"""Regenerate Azure Text Analytics sentiment metadata for a CSV text column.

Credentials are read from environment variables. The preferred names are:

    TEXT_ANALYTICS_SUBSCRIPTION_KEY
    TEXT_ANALYTICS_ENDPOINT

Common Azure aliases such as AZURE_TEXT_ANALYTICS_KEY, AZURE_TEXT_ANALYTICS_ENDPOINT,
LANGUAGE_KEY, and LANGUAGE_ENDPOINT are also accepted.
"""

from __future__ import annotations

import argparse
import logging
import os
import sys
import time
from dataclasses import dataclass
from dataclasses import field
from pathlib import Path

LOGGER = logging.getLogger("sentiment_analytics")

UTTERANCE_COLUMNS = ["utt_sentiment", "utt_pos_score", "utt_neu_score", "utt_neg_score"]
SENTENCE_COLUMNS = [
    "SUID",
    "sentence_split",
    "sentence_idx",
    "sentence_sentiment",
    "pos_score",
    "neu_score",
    "neg_score",
]


@dataclass
class Score:
    positive: float = 0.0
    neutral: float = 0.0
    negative: float = 0.0


@dataclass
class SentenceResult:
    text: str = ""
    sentiment: str | None = None
    confidence_scores: Score = field(default_factory=Score)


@dataclass
class SentimentResult:
    sentiment: str | None = None
    confidence_scores: Score = field(default_factory=Score)
    sentences: list[SentenceResult] | None = None


def env_value(*names: str) -> str:
    for name in names:
        value = os.environ.get(name)
        if value:
            return value
    raise RuntimeError(f"Missing required environment variable. Tried: {', '.join(names)}")


def output_paths(input_path: Path, utterance_output: str | None, sentence_output: str | None) -> tuple[Path, Path]:
    utterance_name = input_path.name.replace("_main.csv", "_utterance_sentiment_analytics.csv")
    if utterance_name == input_path.name:
        utterance_name = f"{input_path.stem}_utterance_sentiment_analytics.csv"
    sentence_name = utterance_name.replace("_utterance_sentiment_analytics.csv", "_sentence_sentiment_analytics.csv")

    utterance_path = Path(utterance_output) if utterance_output else input_path.with_name(utterance_name)
    sentence_path = Path(sentence_output) if sentence_output else utterance_path.with_name(sentence_name)
    if utterance_path.suffix.lower() != ".csv":
        utterance_path = utterance_path / utterance_name
    if sentence_path.suffix.lower() != ".csv":
        sentence_path = sentence_path / sentence_name
    return utterance_path, sentence_path


def confirm_cost(total_rows: int, assume_yes: bool, dry_run: bool) -> None:
    LOGGER.info("Rows queued for sentiment analysis: %s", total_rows)
    if dry_run or assume_yes:
        return

    reply = input("This Azure Text Analytics job may have a cost. Continue? (y/n): ")
    if reply.lower().strip() not in {"y", "yes"}:
        raise SystemExit("Cancelled by user.")


def build_client():
    from azure.ai.textanalytics import TextAnalyticsClient
    from azure.core.credentials import AzureKeyCredential

    key = env_value("TEXT_ANALYTICS_SUBSCRIPTION_KEY", "AZURE_TEXT_ANALYTICS_KEY", "LANGUAGE_KEY")
    endpoint = env_value("TEXT_ANALYTICS_ENDPOINT", "AZURE_TEXT_ANALYTICS_ENDPOINT", "LANGUAGE_ENDPOINT")
    return TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))


def fallback_result() -> SentimentResult:
    return SentimentResult(sentences=[SentenceResult()])


def analyze_text(client, text: str, args: argparse.Namespace):
    for attempt in range(args.retries + 1):
        try:
            response = client.analyze_sentiment(documents=[text], language=args.language)[0]
            if getattr(response, "is_error", False):
                raise RuntimeError(response)
            return response
        except Exception:
            if attempt >= args.retries:
                if args.continue_on_error:
                    LOGGER.exception("Sentiment analysis failed; writing zero scores.")
                    return fallback_result()
                raise
            time.sleep(args.retry_sleep)
    return fallback_result()


def checked_text(text: str, row_idx: int, args: argparse.Namespace) -> str | None:
    if len(text) <= args.max_chars_per_text:
        return text

    message = (
        f"Row {row_idx} has {len(text)} characters; "
        f"Text Analytics limit is {args.max_chars_per_text}."
    )
    if args.truncate:
        LOGGER.warning("%s Truncating.", message)
        return text[: args.max_chars_per_text]
    if args.continue_on_error:
        LOGGER.warning("%s Writing zero scores.", message)
        return None
    raise ValueError(message)


def scores(value) -> tuple[float, float, float]:
    return (
        float(getattr(value, "positive", 0.0)),
        float(getattr(value, "neutral", 0.0)),
        float(getattr(value, "negative", 0.0)),
    )


def result_rows(
    row_id: str,
    text: str,
    response,
    uid_col: str,
    text_col: str,
) -> tuple[dict[str, object], list[dict[str, object]]]:
    pos, neu, neg = scores(response.confidence_scores)
    utterance_row = {
        uid_col: row_id,
        text_col: text,
        "utt_sentiment": response.sentiment,
        "utt_pos_score": pos,
        "utt_neu_score": neu,
        "utt_neg_score": neg,
    }

    sentence_rows: list[dict[str, object]] = []
    cursor = 0
    for idx, sentence in enumerate(response.sentences or [], start=1):
        sentence_text = str(sentence.text)
        start = cursor
        stop = start + len(sentence_text)
        cursor = stop + 1
        sent_pos, sent_neu, sent_neg = scores(sentence.confidence_scores)
        sentence_rows.append(
            {
                "SUID": f"{row_id}-[{start},{stop}]",
                "sentence_split": sentence_text,
                "sentence_idx": idx,
                "sentence_sentiment": sentence.sentiment,
                "pos_score": sent_pos,
                "neu_score": sent_neu,
                "neg_score": sent_neg,
            }
        )
    return utterance_row, sentence_rows


def run(args: argparse.Namespace) -> tuple[Path, Path] | None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    import pandas as pd

    input_path = Path(args.input)
    utterance_path, sentence_path = output_paths(input_path, args.utterance_output, args.sentence_output)
    records_dir = utterance_path.with_suffix("").parent / "records"
    utterance_prefix = records_dir / utterance_path.stem
    sentence_prefix = records_dir / sentence_path.stem

    frame = pd.read_csv(input_path)
    for column in (args.uid_col, args.text_col):
        if column not in frame.columns:
            raise ValueError(f"Column not found in input CSV: {column}")

    checkpoint_count = (len(frame) + args.rows_per_checkpoint - 1) // args.rows_per_checkpoint
    LOGGER.info("Input: %s", input_path)
    LOGGER.info("Utterance output: %s", utterance_path)
    LOGGER.info("Sentence output: %s", sentence_path)
    LOGGER.info("Checkpoints: %s", checkpoint_count)
    confirm_cost(len(frame), args.yes, args.dry_run)

    if args.dry_run:
        return None

    client = build_client()
    records_dir.mkdir(parents=True, exist_ok=True)
    utterance_path.parent.mkdir(parents=True, exist_ok=True)
    sentence_path.parent.mkdir(parents=True, exist_ok=True)

    for checkpoint_idx, start in enumerate(range(0, len(frame), args.rows_per_checkpoint)):
        stop = min(start + args.rows_per_checkpoint, len(frame))
        utterance_record = Path(f"{utterance_prefix}_{checkpoint_idx:03d}.csv")
        sentence_record = Path(f"{sentence_prefix}_{checkpoint_idx:03d}.csv")
        if args.resume and utterance_record.exists() and sentence_record.exists():
            LOGGER.info("Skipping existing checkpoint %s", checkpoint_idx)
            continue

        utterance_rows: list[dict[str, object]] = []
        sentence_rows: list[dict[str, object]] = []
        for row_idx in range(start, stop):
            row_id = str(frame.iloc[row_idx][args.uid_col])
            original_text = str(frame.iloc[row_idx][args.text_col])
            text = checked_text(original_text, row_idx, args)
            response = fallback_result() if text is None else analyze_text(client, text, args)
            utterance_row, row_sentence_rows = result_rows(
                row_id,
                original_text,
                response,
                args.uid_col,
                args.text_col,
            )
            utterance_rows.append(utterance_row)
            sentence_rows.extend(row_sentence_rows)
            if args.sleep:
                time.sleep(args.sleep)

        pd.DataFrame(utterance_rows, columns=[args.uid_col, args.text_col, *UTTERANCE_COLUMNS]).to_csv(
            utterance_record,
            index=False,
            encoding="utf-8-sig",
        )
        pd.DataFrame(sentence_rows, columns=SENTENCE_COLUMNS).to_csv(
            sentence_record,
            index=False,
            encoding="utf-8-sig",
        )
        LOGGER.info("Wrote checkpoint %s/%s", checkpoint_idx + 1, checkpoint_count)

    utterance_pieces = [
        pd.read_csv(f"{utterance_prefix}_{idx:03d}.csv", keep_default_na=False)
        for idx in range(checkpoint_count)
    ]
    sentence_pieces = [
        pd.read_csv(f"{sentence_prefix}_{idx:03d}.csv", keep_default_na=False)
        for idx in range(checkpoint_count)
    ]
    pd.concat(utterance_pieces, ignore_index=True).to_csv(utterance_path, index=False, encoding="utf-8-sig")
    pd.concat(sentence_pieces, ignore_index=True).to_csv(sentence_path, index=False, encoding="utf-8-sig")
    LOGGER.info("Wrote final sentiment files: %s, %s", utterance_path, sentence_path)
    return utterance_path, sentence_path


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Input CSV file.")
    parser.add_argument("--utterance-output", help="Utterance-level output CSV file or directory.")
    parser.add_argument("--sentence-output", help="Sentence-level output CSV file or directory.")
    parser.add_argument("--uid-col", default="UID")
    parser.add_argument("--text-col", default="SEG")
    parser.add_argument("--rows-per-checkpoint", type=int, default=500)
    parser.add_argument("--language", default="en")
    parser.add_argument("--max-chars-per-text", type=int, default=5120)
    parser.add_argument("--sleep", type=float, default=0.065, help="Delay between requests.")
    parser.add_argument("--retries", type=int, default=1)
    parser.add_argument("--retry-sleep", type=float, default=1.0)
    parser.add_argument("--truncate", action="store_true", help="Truncate texts over the API limit.")
    parser.add_argument("--continue-on-error", action="store_true", help="Write zero scores when a row fails.")
    parser.add_argument("--resume", action="store_true", help="Reuse existing checkpoint CSV files.")
    parser.add_argument("--dry-run", action="store_true", help="Plan the job without calling Azure.")
    parser.add_argument("--yes", action="store_true", help="Skip the cost confirmation prompt.")
    return parser.parse_args(argv)


if __name__ == "__main__":
    run(parse_args(sys.argv[1:]))
