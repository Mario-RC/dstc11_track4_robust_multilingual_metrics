"""Generate paraphrases for a CSV text column with Parrot.

The script first tries an installed Parrot package and then falls back to the
local historical Parrot snapshot. The snapshot is intentionally ignored by Git.
"""

from __future__ import annotations

import argparse
import importlib.util
import logging
import sys
import types
from pathlib import Path

LOGGER = logging.getLogger("generate_paraphrases")


def ensure_package(name: str) -> None:
    if name not in sys.modules:
        module = types.ModuleType(name)
        module.__path__ = []
        sys.modules[name] = module


def load_module(module_name: str, path: Path):
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load module {module_name} from {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def load_local_parrot(parrot_root: Path):
    parrot_package = parrot_root / "parrot"
    filters_path = parrot_package / "filters.py"
    parrot_path = parrot_package / "parrot.py"
    if not filters_path.exists() or not parrot_path.exists():
        raise RuntimeError(f"Local Parrot snapshot not found under {parrot_root}")

    for package in (
        "dstc11",
        "dstc11.paraphrase",
        "dstc11.paraphrase.Parrot_Paraphraser",
        "dstc11.paraphrase.Parrot_Paraphraser.parrot",
    ):
        ensure_package(package)

    load_module("dstc11.paraphrase.Parrot_Paraphraser.parrot.filters", filters_path)
    module = load_module("dstc11.paraphrase.Parrot_Paraphraser.parrot.parrot", parrot_path)
    return module.Parrot


def load_parrot(model_tag: str, parrot_root: Path | None):
    try:
        from parrot.parrot import Parrot
    except ImportError as exc:
        if parrot_root and parrot_root.exists():
            Parrot = load_local_parrot(parrot_root)
            return Parrot(model_tag=model_tag)
        raise RuntimeError(
            "Parrot is not importable. Install the Parrot paraphraser package "
            "or provide the local Parrot_Paraphraser snapshot with --parrot-root."
        ) from exc
    return Parrot(model_tag=model_tag)


def normalize_paraphrase_item(item: object) -> str:
    if isinstance(item, (list, tuple)) and item:
        return str(item[0])
    return str(item)


def normalize_paraphrase_batch(batch: object) -> list[str]:
    if not batch:
        return []
    if isinstance(batch, (list, tuple)):
        return [normalize_paraphrase_item(item) for item in batch]
    return [str(batch)]


def run(args: argparse.Namespace) -> Path:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    import pandas as pd
    from tqdm import tqdm

    input_path = Path(args.input)
    output_path = Path(args.output) if args.output else input_path.with_name(f"{input_path.stem}_para.csv")

    frame = pd.read_csv(input_path)
    if args.text_col not in frame.columns:
        raise ValueError(f"Column not found in input CSV: {args.text_col}")

    parrot_root = Path(args.parrot_root) if args.parrot_root else None
    parrot = load_parrot(args.model_tag, parrot_root)
    paraphrases: list[list[str]] = []
    texts = frame[args.text_col].fillna("").astype(str).tolist()

    for start in tqdm(range(0, len(texts), args.batch_size), desc="Paraphrasing"):
        batch = texts[start : start + args.batch_size]
        _, batch_paraphrases = parrot.augment(
            input_phrase_lst=batch,
            use_gpu=args.use_gpu,
            diversity_ranker=args.diversity_ranker,
            do_diverse=args.diverse,
            max_return_phrases=args.max_return_phrases,
            max_length=args.max_length,
            adequacy_threshold=args.adequacy_threshold,
            fluency_threshold=args.fluency_threshold,
        )
        paraphrases.extend(normalize_paraphrase_batch(row) for row in batch_paraphrases)

    frame[args.output_col] = paraphrases
    output_path.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(output_path, index=False, encoding="utf-8")
    LOGGER.info("Wrote %s", output_path)
    return output_path


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Input CSV file.")
    parser.add_argument("--output", help="Output CSV file.")
    parser.add_argument("--text-col", default="SEG")
    parser.add_argument("--output-col", default="PARAPHRASES")
    parser.add_argument("--model-tag", default="prithivida/parrot_parrot_paraphraser_on_T5")
    parser.add_argument(
        "--parrot-root",
        default=str(Path(__file__).resolve().parent / "Parrot_Paraphraser"),
        help="Optional local Parrot_Paraphraser snapshot.",
    )
    parser.add_argument("--batch-size", type=int, default=24)
    parser.add_argument("--max-return-phrases", type=int, default=40)
    parser.add_argument("--max-length", type=int, default=32)
    parser.add_argument("--adequacy-threshold", type=float, default=0.85)
    parser.add_argument("--fluency-threshold", type=float, default=0.8)
    parser.add_argument("--diversity-ranker", default="levenshtein")
    parser.add_argument("--diverse", action="store_true")
    parser.add_argument("--use-gpu", action="store_true")
    return parser.parse_args(argv)


if __name__ == "__main__":
    run(parse_args(sys.argv[1:]))
