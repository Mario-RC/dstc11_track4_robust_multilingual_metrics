"""Compute sentence-embedding similarity scores for translation files."""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

LOGGER = logging.getLogger("compute_translation_similarity")


def encode(model, texts, batch_size: int):
    return model.encode(
        texts.fillna("").astype(str).tolist(),
        batch_size=batch_size,
        convert_to_numpy=True,
        normalize_embeddings=True,
        show_progress_bar=True,
    )


def pairwise_cosine(left, right) -> list[float]:
    import numpy as np

    return np.sum(left * right, axis=1).astype(float).tolist()


def require_columns(frame, columns: list[str]) -> None:
    missing = [column for column in columns if column not in frame.columns]
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")


def run(args: argparse.Namespace) -> Path:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    import pandas as pd
    from sentence_transformers import SentenceTransformer

    input_path = Path(args.input)
    output_path = Path(args.output) if args.output else input_path

    frame = pd.read_csv(input_path)
    require_columns(frame, [args.source_col, args.translation_col])

    LOGGER.info("Loading multilingual model 1: %s", args.multilingual_model_1)
    multilingual_1 = SentenceTransformer(args.multilingual_model_1)
    source_multi_1 = encode(multilingual_1, frame[args.source_col], args.batch_size)
    translation_multi_1 = encode(multilingual_1, frame[args.translation_col], args.batch_size)
    frame[args.cos_multi_1_st_col] = pairwise_cosine(source_multi_1, translation_multi_1)

    LOGGER.info("Loading multilingual model 2: %s", args.multilingual_model_2)
    multilingual_2 = SentenceTransformer(args.multilingual_model_2)
    source_multi_2 = encode(multilingual_2, frame[args.source_col], args.batch_size)
    translation_multi_2 = encode(multilingual_2, frame[args.translation_col], args.batch_size)
    frame[args.cos_multi_2_st_col] = pairwise_cosine(source_multi_2, translation_multi_2)

    if args.backtranslation_col in frame.columns and not args.skip_backtranslation:
        LOGGER.info("Computing backtranslation similarities from column: %s", args.backtranslation_col)
        backtranslation_multi_1 = encode(multilingual_1, frame[args.backtranslation_col], args.batch_size)
        backtranslation_multi_2 = encode(multilingual_2, frame[args.backtranslation_col], args.batch_size)
        frame[args.cos_multi_1_tb_col] = pairwise_cosine(translation_multi_1, backtranslation_multi_1)
        frame[args.cos_multi_2_tb_col] = pairwise_cosine(translation_multi_2, backtranslation_multi_2)

        LOGGER.info("Loading monolingual model: %s", args.monolingual_model)
        monolingual = SentenceTransformer(args.monolingual_model)
        source_mono = encode(monolingual, frame[args.source_col], args.batch_size)
        backtranslation_mono = encode(monolingual, frame[args.backtranslation_col], args.batch_size)
        frame[args.cos_mono_sb_col] = pairwise_cosine(source_mono, backtranslation_mono)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(output_path, index=False, encoding="utf-8")
    LOGGER.info("Wrote %s", output_path)
    return output_path


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Input CSV file.")
    parser.add_argument("--output", help="Output CSV file. Defaults to overwriting input.")
    parser.add_argument("--source-col", default="SEG")
    parser.add_argument("--translation-col", default="TRANSLATION")
    parser.add_argument("--backtranslation-col", default="BACKTRANSLATION")
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--skip-backtranslation", action="store_true")
    parser.add_argument("--monolingual-model", default="paraphrase-TinyBERT-L6-v2")
    parser.add_argument("--multilingual-model-1", default="distiluse-base-multilingual-cased-v1")
    parser.add_argument("--multilingual-model-2", default="paraphrase-xlm-r-multilingual-v1")
    parser.add_argument("--cos-mono-sb-col", default="COS_SIM_MONO_SB")
    parser.add_argument("--cos-multi-1-st-col", default="COS_SIM_MULTI_1_ST")
    parser.add_argument("--cos-multi-2-st-col", default="COS_SIM_MULTI_2_ST")
    parser.add_argument("--cos-multi-1-tb-col", default="COS_SIM_MULTI_1_TB")
    parser.add_argument("--cos-multi-2-tb-col", default="COS_SIM_MULTI_2_TB")
    return parser.parse_args(argv)


if __name__ == "__main__":
    run(parse_args(sys.argv[1:]))
