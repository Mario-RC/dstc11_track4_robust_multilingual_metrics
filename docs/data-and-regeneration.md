# Data and Regeneration

This repository intentionally keeps large data files out of GitHub. The public source of the DSTC11 Track 4 train/development release is Hugging Face:

```text
https://huggingface.co/datasets/mario-rc/dstc11.t4
```

Download the public dataset files from Hugging Face into:

```text
data/DSTC_11_Track_4/
```

Recommended download command. It requires `huggingface_hub`:

```bash
python - <<'PY'
from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="mario-rc/dstc11.t4",
    repo_type="dataset",
    allow_patterns=["DSTC_11_Track_4/**"],
    local_dir="data",
)
PY
```

The `data/` directory is ignored by Git except for `data/README.md`.

Held-out test data is intentionally not part of the public Hugging Face release. If test data is needed for research or evaluation, request access from the DSTC11 Track 4 organizers.

The recommended Hugging Face dataset card is maintained in:

```text
docs/huggingface-dataset-card.md
```

## Local MTQE Cache

`tools/mtqe/data/` is a local historical cache copied from the original MTQE workspace. It contains intermediate CSV files, translation/backtranslation variants, paraphrase files, and cosine-similarity outputs.

Do not upload `tools/mtqe/data/` to GitHub. It is ignored by `.gitignore`.

The useful public assets are the scripts that regenerate derived scores from the Hugging Face dataset:

```text
tools/metadata/content_moderator.py
tools/metadata/sentiment_analytics.py
tools/mtqe/compute_translation_similarity.py
tools/paraphrase/compute_paraphrase_similarity.py
```

## Regenerate Translation Similarity Scores

Install the MTQE dependencies:

```bash
python -m pip install -r tools/mtqe/requirements.txt
```

Then run the MTQE similarity script on any multilingual CSV from the downloaded dataset:

```bash
python tools/mtqe/compute_translation_similarity.py \
  --input data/DSTC_11_Track_4/task1/dev/en_es/convai2-grade_multilingual_en_es.csv \
  --output outputs/mtqe/convai2-grade_multilingual_en_es_scored.csv
```

For files with `SEG`, `TRANSLATION`, and `BACKTRANSLATION`, the script computes source-translation, translation-backtranslation, and source-backtranslation similarities:

```text
COS_SIM_MULTI_1_ST
COS_SIM_MULTI_2_ST
COS_SIM_MULTI_1_TB
COS_SIM_MULTI_2_TB
COS_SIM_MONO_SB
```

For files without `BACKTRANSLATION`, use:

```bash
python tools/mtqe/compute_translation_similarity.py \
  --input data/DSTC_11_Track_4/task1/train/zh_en/ECM_multilingual_zh_en.csv \
  --output outputs/mtqe/ECM_multilingual_zh_en_scored.csv \
  --skip-backtranslation
```

These scores are regenerated locally with sentence-transformer models. No paid API is required for this step, although downloading models requires internet access the first time.

## Regenerate Paraphrase Similarity Scores

Install the paraphrase dependencies:

```bash
python -m pip install -r tools/paraphrase/requirements.txt
```

Use the paraphrase scoring script on any Task 2 file with `SEG` and `PARAPHRASES` columns:

```bash
python tools/paraphrase/compute_paraphrase_similarity.py \
  --input data/DSTC_11_Track_4/task2/dev/convai2-grade_paraphrases.csv \
  --output outputs/paraphrase/convai2-grade_paraphrases_scored.csv
```

This computes source-paraphrase cosine similarities using a local sentence-transformer model. No paid API is required for this scoring step.

## Regenerate Azure Metadata

The dataset includes Azure-derived metadata files for moderation and sentiment analysis. These files are already included in the prepared dataset release, so most users do not need to regenerate them.

If regeneration is needed, install the optional Azure dependencies:

```bash
python -m pip install -r tools/metadata/requirements.txt
```

Content Moderator metadata requires credentials in environment variables:

```bash
export CONTENT_MODERATOR_SUBSCRIPTION_KEY="<content-moderator-key>"
export CONTENT_MODERATOR_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

python tools/metadata/content_moderator.py \
  --input data/DSTC_11_Track_4/metadata/train/en/DAILYD/DAILYD_main.csv \
  --output outputs/metadata/DAILYD_content_moderator.csv \
  --yes
```

Sentiment metadata requires Text Analytics credentials:

```bash
export TEXT_ANALYTICS_SUBSCRIPTION_KEY="<text-analytics-key>"
export TEXT_ANALYTICS_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"

python tools/metadata/sentiment_analytics.py \
  --input data/DSTC_11_Track_4/metadata/train/en/DAILYD/DAILYD_main.csv \
  --utterance-output outputs/metadata/DAILYD_utterance_sentiment_analytics.csv \
  --sentence-output outputs/metadata/DAILYD_sentence_sentiment_analytics.csv \
  --yes
```

These steps may incur Azure costs. Never commit real service keys, executed notebooks, or local credential files.

## What May Require Paid Services

Regenerating the original translations, backtranslations, Content Moderator metadata, or sentiment metadata from raw text may require external paid services, depending on the provider used. The public train/development release already includes the open data needed for most reuse cases, so normal users should use the released Hugging Face files instead of re-running paid service jobs.

## What Goes to GitHub

Upload:

```text
README.md
dstc11/
img/
docs/
tools/
data/README.md
```

Do not upload:

```text
data/DSTC_11_Track_4/
local held-out test data
tools/mtqe/data/
tools/mtqe/results/
tools/mtqe/logs/
tools/paraphrase/Parrot_Paraphraser/
tools/*/legacy/
outputs/
credentials, notebooks with executed secrets, local environments, or model caches
```

## Public CSV and Spreadsheet Metadata Hygiene

Do not remove dataset columns just because they describe the dialogue schema. For example, columns such as `UID`, `SID`, `SEG`, `TRANSLATION`, `BACKTRANSLATION`, or `PARAPHRASES` are dataset content, not file metadata.

Before adding CSV or spreadsheet files to GitHub, review file-level metadata and publication risk:

```text
CSV files usually do not carry embedded document properties, but their content should still be intentionally public
Excel/OpenDocument files may contain authors, editing timestamps, hidden sheets, comments, revision history, external links, and local paths
avoid publishing spreadsheets unless that embedded metadata has been explicitly reviewed and cleaned
prefer CSV exports when possible because they strip workbook-level document metadata
```

Excel and OpenDocument spreadsheet files are ignored by default in `.gitignore`. If a spreadsheet ever needs to be published, review and sanitize its embedded metadata first, then add it intentionally.
