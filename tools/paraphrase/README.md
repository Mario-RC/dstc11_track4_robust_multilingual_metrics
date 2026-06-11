# Paraphrase Tools

This directory contains clean utilities for paraphrase generation and paraphrase similarity scoring.

Use the Hugging Face dataset as the input source and write generated artifacts under `outputs/` or another ignored local directory. See [../../docs/data-and-regeneration.md](../../docs/data-and-regeneration.md).

## Generate Paraphrases

`generate_paraphrases.py` uses an installed Parrot package when available. If not, it can use the local `Parrot_Paraphraser/` snapshot through `--parrot-root`; that snapshot is preserved locally but ignored by Git.

```bash
python tools/paraphrase/generate_paraphrases.py \
  --input tools/paraphrase/examples/sample_input.csv \
  --output outputs/sample_paraphrases.csv \
  --text-col SEG \
  --use-gpu
```

## Score Paraphrases

`compute_paraphrase_similarity.py` computes source-paraphrase similarity scores.

```bash
python tools/paraphrase/compute_paraphrase_similarity.py \
  --input tools/paraphrase/examples/sample_paraphrases.csv \
  --output outputs/sample_paraphrases_scored.csv \
  --source-col SEG \
  --paraphrases-col PARAPHRASES
```

The original Parrot snapshot, generated paraphrase data, logs, and legacy notes are local-only material and ignored by Git.
