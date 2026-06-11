# MTQE and Similarity Tools

`compute_translation_similarity.py` adds sentence-embedding similarity scores to translation CSV files.

## Data Source

Use the public dataset from Hugging Face as input:

```text
https://huggingface.co/datasets/mario-rc/dstc11.t4
```

Place the extracted dataset locally under:

```text
data/DSTC_11_Track_4/
```

`tools/mtqe/data/` is only a local historical cache from the old MTQE workspace. It is ignored by Git and should not be uploaded.

## Regenerate Scores

Example:

```bash
python tools/mtqe/compute_translation_similarity.py \
  --input data/DSTC_11_Track_4/task1/dev/en_es/convai2-grade_multilingual_en_es.csv \
  --output outputs/convai2-grade_multilingual_en_es_scored.csv
```

The script computes:

```text
COS_SIM_MULTI_1_ST
COS_SIM_MULTI_2_ST
COS_SIM_MULTI_1_TB
COS_SIM_MULTI_2_TB
COS_SIM_MONO_SB
```

Backtranslation scores are only produced when the input contains a `BACKTRANSLATION` column. Use `--skip-backtranslation` to compute only source-translation scores.

The generated CSVs should be written under `outputs/` or another ignored local directory.

These derived scores are computed locally with sentence-transformer models. No paid API is required for the score-generation step, although the models may need to be downloaded the first time.

See [../../docs/data-and-regeneration.md](../../docs/data-and-regeneration.md) for the full data policy and regeneration workflow.
