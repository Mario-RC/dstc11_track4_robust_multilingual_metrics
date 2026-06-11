"""Compute similarity scores between source turns and generated paraphrases."""

from __future__ import annotations

import argparse
import ast
import logging
import math
import sys
from pathlib import Path

LOGGER = logging.getLogger("compute_paraphrase_similarity")


def normalize_paraphrase_item(item: object) -> str:
    if isinstance(item, (list, tuple)) and item:
        return str(item[0])
    return str(item)


def parse_paraphrases(value: object) -> list[str]:
    if value is None or (isinstance(value, float) and math.isnan(value)):
        return []
    if isinstance(value, list):
        return [normalize_paraphrase_item(item) for item in value]

    text = str(value).strip()
    if not text or text.lower() == "none":
        return []

    try:
        parsed = ast.literal_eval(text)
    except (SyntaxError, ValueError):
        return [text]

    if parsed is None:
        return []
    if isinstance(parsed, list):
        return [normalize_paraphrase_item(item) for item in parsed]
    return [normalize_paraphrase_item(parsed)]


def pairwise_scores(source_embedding, paraphrase_embeddings) -> list[float]:
    import numpy as np

    if len(paraphrase_embeddings) == 0:
        return []
    return np.sum(source_embedding * paraphrase_embeddings, axis=1).astype(float).tolist()


def run(args: argparse.Namespace) -> Path:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    import numpy as np
    import pandas as pd
    from sentence_transformers import SentenceTransformer

    input_path = Path(args.input)
    output_path = Path(args.output) if args.output else input_path

    frame = pd.read_csv(input_path)
    for column in (args.source_col, args.paraphrases_col):
        if column not in frame.columns:
            raise ValueError(f"Column not found in input CSV: {column}")

    paraphrases = frame[args.paraphrases_col].apply(parse_paraphrases).tolist()
    LOGGER.info("Loading model: %s", args.model)
    model = SentenceTransformer(args.model)

    source_embeddings = model.encode(
        frame[args.source_col].fillna("").astype(str).tolist(),
        batch_size=args.batch_size,
        convert_to_numpy=True,
        normalize_embeddings=True,
        show_progress_bar=True,
    )

    flat_paraphrases = [text for row in paraphrases for text in row]
    flat_embeddings = model.encode(
        flat_paraphrases,
        batch_size=args.batch_size,
        convert_to_numpy=True,
        normalize_embeddings=True,
        show_progress_bar=True,
    ) if flat_paraphrases else np.empty((0, source_embeddings.shape[1]))

    scores: list[list[float]] = []
    cursor = 0
    for source_embedding, row_paraphrases in zip(source_embeddings, paraphrases):
        count = len(row_paraphrases)
        row_embeddings = flat_embeddings[cursor : cursor + count]
        scores.append(pairwise_scores(source_embedding, row_embeddings))
        cursor += count

    frame[args.output_col] = scores
    output_path.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(output_path, index=False, encoding="utf-8")
    LOGGER.info("Wrote %s", output_path)
    return output_path


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Input CSV file.")
    parser.add_argument("--output", help="Output CSV file. Defaults to overwriting input.")
    parser.add_argument("--source-col", default="SEG")
    parser.add_argument("--paraphrases-col", default="PARAPHRASES")
    parser.add_argument("--output-col", default="COS_SIM_MONO_SP")
    parser.add_argument("--model", default="paraphrase-TinyBERT-L6-v2")
    parser.add_argument("--batch-size", type=int, default=64)
    return parser.parse_args(argv)


if __name__ == "__main__":
    run(parse_args(sys.argv[1:]))
