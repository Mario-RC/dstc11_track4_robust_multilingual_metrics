"""Regenerate Azure Content Moderator metadata for a CSV text column.

Credentials are read from environment variables:

    CONTENT_MODERATOR_SUBSCRIPTION_KEY
    CONTENT_MODERATOR_ENDPOINT

The output schema matches the DSTC11 Track 4 metadata files:

    UID, SEG, profanity_terms, sexually_explicit_adult_score,
    sexually_suggestive_mature_score, offensive_score, review_recommended
"""

from __future__ import annotations

import argparse
import logging
import os
import sys
import time
from io import BytesIO
from pathlib import Path

LOGGER = logging.getLogger("content_moderator")

OUTPUT_COLUMNS = [
    "profanity_terms",
    "sexually_explicit_adult_score",
    "sexually_suggestive_mature_score",
    "offensive_score",
    "review_recommended",
]


def env_value(*names: str) -> str:
    for name in names:
        value = os.environ.get(name)
        if value:
            return value
    raise RuntimeError(f"Missing required environment variable. Tried: {', '.join(names)}")


def resolve_output_path(input_path: Path, output: str | None) -> Path:
    default_name = input_path.name.replace("_main.csv", "_content_moderator.csv")
    if default_name == input_path.name:
        default_name = f"{input_path.stem}_content_moderator.csv"

    if output is None:
        return input_path.with_name(default_name)

    candidate = Path(output)
    if candidate.suffix.lower() == ".csv":
        return candidate
    return candidate / default_name


def confirm_cost(total_rows: int, assume_yes: bool, dry_run: bool) -> None:
    LOGGER.info("Rows queued for moderation: %s", total_rows)
    if dry_run or assume_yes:
        return

    reply = input("This Azure Content Moderator job may have a cost. Continue? (y/n): ")
    if reply.lower().strip() not in {"y", "yes"}:
        raise SystemExit("Cancelled by user.")


def build_client():
    from azure.cognitiveservices.vision.contentmoderator import ContentModeratorClient
    from msrest.authentication import CognitiveServicesCredentials

    endpoint = env_value("CONTENT_MODERATOR_ENDPOINT", "AZURE_CONTENT_MODERATOR_ENDPOINT")
    key = env_value("CONTENT_MODERATOR_SUBSCRIPTION_KEY", "AZURE_CONTENT_MODERATOR_KEY")
    return ContentModeratorClient(
        endpoint=endpoint,
        credentials=CognitiveServicesCredentials(key),
    )


def fallback_result() -> dict:
    return {
        "terms": [],
        "classification": {
            "category1": {"score": 0.0},
            "category2": {"score": 0.0},
            "category3": {"score": 0.0},
            "review_recommended": False,
        },
    }


def screen_text(client, text: str, args: argparse.Namespace) -> dict:
    for attempt in range(args.retries + 1):
        try:
            text_stream = BytesIO(text.encode("utf-8"))
            response = client.text_moderation.screen_text(
                text_content_type="text/plain",
                text_content=text_stream,
                classify=True,
                language=args.language,
                autocorrect=args.autocorrect,
                pii=args.pii,
            )
            return response.as_dict()
        except Exception:
            if attempt >= args.retries:
                if args.continue_on_error:
                    LOGGER.exception("Content moderation failed; writing zero scores.")
                    return fallback_result()
                raise
            time.sleep(args.retry_sleep)
    return fallback_result()


def make_row(
    row_id: str,
    text: str,
    response: dict,
    uid_col: str,
    text_col: str,
) -> dict[str, object]:
    terms = response.get("terms") or []
    profanity_terms = ", ".join(str(term.get("term", "")) for term in terms if term.get("term")) or "None"
    classification = response.get("classification") or {}

    def score(category: str) -> float:
        value = (classification.get(category) or {}).get("score", 0.0)
        return round(float(value), 3)

    return {
        uid_col: row_id,
        text_col: text,
        "profanity_terms": profanity_terms,
        "sexually_explicit_adult_score": score("category1"),
        "sexually_suggestive_mature_score": score("category2"),
        "offensive_score": score("category3"),
        "review_recommended": bool(classification.get("review_recommended", False)),
    }


def checked_text(text: str, row_idx: int, args: argparse.Namespace) -> str | None:
    if len(text) <= args.max_chars_per_text:
        return text

    message = (
        f"Row {row_idx} has {len(text)} characters; "
        f"Content Moderator limit is {args.max_chars_per_text}."
    )
    if args.truncate:
        LOGGER.warning("%s Truncating.", message)
        return text[: args.max_chars_per_text]
    if args.continue_on_error:
        LOGGER.warning("%s Writing zero scores.", message)
        return None
    raise ValueError(message)


def run(args: argparse.Namespace) -> Path | None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    import pandas as pd

    input_path = Path(args.input)
    output_path = resolve_output_path(input_path, args.output)
    records_dir = output_path.with_suffix("").parent / "records"
    records_prefix = records_dir / output_path.stem

    frame = pd.read_csv(input_path)
    for column in (args.uid_col, args.text_col):
        if column not in frame.columns:
            raise ValueError(f"Column not found in input CSV: {column}")

    checkpoint_count = (len(frame) + args.rows_per_checkpoint - 1) // args.rows_per_checkpoint
    LOGGER.info("Input: %s", input_path)
    LOGGER.info("Output: %s", output_path)
    LOGGER.info("Checkpoint files: %s_*.csv", records_prefix)
    LOGGER.info("Checkpoints: %s", checkpoint_count)
    confirm_cost(len(frame), args.yes, args.dry_run)

    if args.dry_run:
        return None

    client = build_client()
    records_dir.mkdir(parents=True, exist_ok=True)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    for checkpoint_idx, start in enumerate(range(0, len(frame), args.rows_per_checkpoint)):
        stop = min(start + args.rows_per_checkpoint, len(frame))
        record_path = Path(f"{records_prefix}_{checkpoint_idx:03d}.csv")
        if args.resume and record_path.exists():
            LOGGER.info("Skipping existing checkpoint %s", record_path)
            continue

        rows: list[dict[str, object]] = []
        for row_idx in range(start, stop):
            row_id = str(frame.iloc[row_idx][args.uid_col])
            original_text = str(frame.iloc[row_idx][args.text_col])
            text = checked_text(original_text, row_idx, args)
            response = fallback_result() if text is None else screen_text(client, text, args)
            rows.append(make_row(row_id, original_text, response, args.uid_col, args.text_col))
            if args.sleep:
                time.sleep(args.sleep)

        pd.DataFrame(rows, columns=[args.uid_col, args.text_col, *OUTPUT_COLUMNS]).to_csv(
            record_path,
            index=False,
            encoding="utf-8-sig",
        )
        LOGGER.info("Wrote checkpoint %s/%s: %s", checkpoint_idx + 1, checkpoint_count, record_path)

    pieces = [
        pd.read_csv(f"{records_prefix}_{idx:03d}.csv", keep_default_na=False)
        for idx in range(checkpoint_count)
    ]
    pd.concat(pieces, ignore_index=True).to_csv(output_path, index=False, encoding="utf-8-sig")
    LOGGER.info("Wrote final content moderator file: %s", output_path)
    return output_path


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Input CSV file.")
    parser.add_argument("--output", help="Output CSV file or directory.")
    parser.add_argument("--uid-col", default="UID")
    parser.add_argument("--text-col", default="SEG")
    parser.add_argument("--rows-per-checkpoint", type=int, default=500)
    parser.add_argument("--language", default="eng")
    parser.add_argument("--max-chars-per-text", type=int, default=1024)
    parser.add_argument("--sleep", type=float, default=0.11, help="Delay between requests.")
    parser.add_argument("--retries", type=int, default=1)
    parser.add_argument("--retry-sleep", type=float, default=1.0)
    parser.add_argument("--autocorrect", action="store_true")
    parser.add_argument("--pii", action="store_true")
    parser.add_argument("--truncate", action="store_true", help="Truncate texts over the API limit.")
    parser.add_argument("--continue-on-error", action="store_true", help="Write zero scores when a row fails.")
    parser.add_argument("--resume", action="store_true", help="Reuse existing checkpoint CSV files.")
    parser.add_argument("--dry-run", action="store_true", help="Plan the job without calling Azure.")
    parser.add_argument("--yes", action="store_true", help="Skip the cost confirmation prompt.")
    return parser.parse_args(argv)


if __name__ == "__main__":
    run(parse_args(sys.argv[1:]))
