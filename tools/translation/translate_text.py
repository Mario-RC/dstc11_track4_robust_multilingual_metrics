"""Translate CSV text columns with Azure Translator.

Credentials are read from environment variables:

    TRANSLATOR_TEXT_SUBSCRIPTION_KEY
    TRANSLATOR_TEXT_ENDPOINT
    TRANSLATOR_TEXT_REGION

The script writes checkpoint files under ``records/`` next to the output file so
large translation jobs can be resumed safely.
"""

from __future__ import annotations

import argparse
import logging
import os
import re
import sys
import uuid
from pathlib import Path
from urllib.parse import urljoin

LOGGER = logging.getLogger("translate_text")
PROFANITY_PATTERN = re.compile(r"<profanity>(.*?)</profanity>", re.DOTALL)


def env_value(name: str, default: str | None = None) -> str:
    value = os.environ.get(name, default)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def resolve_output_path(csv_path: Path, save_path: str | None, source: str, target: str) -> Path:
    default_name = csv_path.name.replace("_main.csv", f"_translation_{source}2{target}.csv")
    if default_name == csv_path.name:
        default_name = f"{csv_path.stem}_translation_{source}2{target}.csv"

    if save_path is None:
        return csv_path.with_name(default_name)

    candidate = Path(save_path)
    if candidate.suffix.lower() == ".csv":
        return candidate
    return candidate / default_name


def build_checkpoints(
    frame,
    text_col: str,
    rows_per_checkpoint: int,
    batch_size: int,
    max_chars_per_text: int,
    max_chars_per_request: int,
) -> list[list[list[int]]]:
    if rows_per_checkpoint <= 0:
        raise ValueError("rows_per_checkpoint must be greater than 0")
    if not 1 <= batch_size <= 100:
        raise ValueError("batch_size must be between 1 and 100")

    checkpoints: list[list[list[int]]] = []
    for start in range(0, len(frame), rows_per_checkpoint):
        stop = min(start + rows_per_checkpoint, len(frame))
        checkpoint: list[list[int]] = []
        batch: list[int] = []
        batch_chars = 0

        for row_idx in range(start, stop):
            text = str(frame.iloc[row_idx][text_col])
            text_chars = len(text)
            if text_chars > max_chars_per_text:
                raise ValueError(
                    f"Row {row_idx} has {text_chars} characters; "
                    f"limit is {max_chars_per_text}"
                )

            would_exceed = (
                len(batch) >= batch_size
                or (batch and batch_chars + text_chars > max_chars_per_request)
            )
            if would_exceed:
                checkpoint.append(batch)
                batch = []
                batch_chars = 0

            batch.append(row_idx)
            batch_chars += text_chars

        if batch:
            checkpoint.append(batch)
        checkpoints.append(checkpoint)

    return checkpoints


def total_characters(frame: pd.DataFrame, text_col: str) -> int:
    return int(frame[text_col].fillna("").astype(str).str.len().sum())


def confirm_cost(total_chars: int, assume_yes: bool, dry_run: bool) -> None:
    LOGGER.info("Total characters queued for translation: %s", total_chars)
    if dry_run or assume_yes:
        return

    reply = input("This Azure Translator job may have a cost. Continue? (y/n): ")
    if reply.lower().strip() not in {"y", "yes"}:
        raise SystemExit("Cancelled by user.")


def translate_batch(
    session: requests.Session,
    url: str,
    headers: dict[str, str],
    texts: list[str],
    timeout: int,
) -> list[dict]:
    response = session.post(url, headers=headers, json=[{"text": text} for text in texts], timeout=timeout)
    response.raise_for_status()
    payload = response.json()
    if not isinstance(payload, list):
        raise RuntimeError(f"Unexpected Azure Translator response: {payload}")
    return payload


def extract_translation(payload: dict, row_id: str) -> tuple[str, str]:
    try:
        translated = payload["translations"][0]["text"]
    except (KeyError, IndexError, TypeError) as exc:
        raise RuntimeError(f"Missing translation for row {row_id}: {payload}") from exc

    profanity = ", ".join(PROFANITY_PATTERN.findall(translated)) or "None"
    cleaned = translated.replace("<profanity>", "").replace("</profanity>", "")
    return cleaned, profanity


def run(args: argparse.Namespace) -> Path | None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    import pandas as pd

    csv_path = Path(args.csv_path)
    output_path = resolve_output_path(csv_path, args.save_path, args.from_language, args.to_language)
    records_dir = output_path.with_suffix("").parent / "records"
    records_prefix = records_dir / output_path.stem

    frame = pd.read_csv(csv_path)
    for required_col in (args.uid_col, args.seg_col):
        if required_col not in frame.columns:
            raise ValueError(f"Column not found in input CSV: {required_col}")

    checkpoints = build_checkpoints(
        frame=frame,
        text_col=args.seg_col,
        rows_per_checkpoint=args.rows_per_checkpoint,
        batch_size=args.batch_size,
        max_chars_per_text=args.max_chars_per_text,
        max_chars_per_request=args.max_chars_per_request,
    )

    LOGGER.info("Input: %s", csv_path)
    LOGGER.info("Output: %s", output_path)
    LOGGER.info("Checkpoint files: %s_*.csv", records_prefix)
    LOGGER.info("Checkpoints: %s", len(checkpoints))
    confirm_cost(total_characters(frame, args.seg_col), args.yes, args.dry_run)

    if args.dry_run:
        return None

    import requests

    subscription_key = env_value("TRANSLATOR_TEXT_SUBSCRIPTION_KEY")
    endpoint = env_value("TRANSLATOR_TEXT_ENDPOINT").rstrip("/") + "/"
    region = args.region or os.environ.get("TRANSLATOR_TEXT_REGION")
    if not region:
        raise RuntimeError("Set --region or TRANSLATOR_TEXT_REGION")

    url = urljoin(endpoint, "translate")
    params = (
        f"?api-version=3.0&from={args.from_language}&to={args.to_language}"
        "&profanityAction=Marked&profanityMarker=Tag"
    )
    headers = {
        "Ocp-Apim-Subscription-Key": subscription_key,
        "Ocp-Apim-Subscription-Region": region,
        "Content-type": "application/json",
        "X-ClientTraceId": str(uuid.uuid4()),
    }

    records_dir.mkdir(parents=True, exist_ok=True)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    session = requests.Session()
    for checkpoint_idx, checkpoint in enumerate(checkpoints):
        record_path = Path(f"{records_prefix}_{checkpoint_idx:03d}.csv")
        if args.resume and record_path.exists():
            LOGGER.info("Skipping existing checkpoint %s", record_path)
            continue

        rows: list[dict[str, object]] = []
        for batch in checkpoint:
            texts = [str(frame.iloc[row_idx][args.seg_col]) for row_idx in batch]
            payload = translate_batch(session, url + params, headers, texts, args.timeout)

            for row_idx, response_item in zip(batch, payload):
                row_id = str(frame.iloc[row_idx][args.uid_col])
                translated, profanity = extract_translation(response_item, row_id)
                row = frame.iloc[row_idx].to_dict()
                row[args.translation_col] = translated
                row[args.profanity_col] = profanity
                rows.append(row)

        output_columns = [*frame.columns, args.translation_col, args.profanity_col]
        pd.DataFrame(rows, columns=output_columns).to_csv(record_path, index=False, encoding="utf-8-sig")
        LOGGER.info("Wrote checkpoint %s/%s: %s", checkpoint_idx + 1, len(checkpoints), record_path)

    pieces = [
        pd.read_csv(f"{records_prefix}_{idx:03d}.csv", keep_default_na=False)
        for idx in range(len(checkpoints))
    ]
    pd.concat(pieces, ignore_index=True).to_csv(output_path, index=False, encoding="utf-8-sig")
    LOGGER.info("Wrote final translation file: %s", output_path)
    return output_path


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv-path", required=True, help="Input CSV file.")
    parser.add_argument("--save-path", help="Output CSV file or directory.")
    parser.add_argument("--from-language", default="en")
    parser.add_argument("--to-language", default="es")
    parser.add_argument("--region", help="Azure Translator region.")
    parser.add_argument("--rows-per-checkpoint", type=int, default=500)
    parser.add_argument("--batch-size", type=int, default=100)
    parser.add_argument("--max-chars-per-text", type=int, default=10_000)
    parser.add_argument("--max-chars-per-request", type=int, default=10_000)
    parser.add_argument("--uid-col", default="UID")
    parser.add_argument("--seg-col", default="SEG")
    parser.add_argument("--translation-col", default="TRANSLATION")
    parser.add_argument("--profanity-col", default="profanity")
    parser.add_argument("--timeout", type=int, default=60)
    parser.add_argument("--resume", action="store_true", help="Reuse existing checkpoint CSV files.")
    parser.add_argument("--dry-run", action="store_true", help="Plan the job without calling Azure.")
    parser.add_argument("--yes", action="store_true", help="Skip the cost confirmation prompt.")
    return parser.parse_args(argv)


if __name__ == "__main__":
    run(parse_args(sys.argv[1:]))
