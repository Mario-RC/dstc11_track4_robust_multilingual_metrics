# Metadata Tools

These utilities regenerate optional Azure-derived metadata from local CSV files. They are provided for reproducibility; most users should download the prepared dataset from Hugging Face instead of rerunning paid services.

## Setup

```bash
python -m pip install -r tools/metadata/requirements.txt
```

## Content Moderator

Credentials are read from environment variables:

```bash
export CONTENT_MODERATOR_SUBSCRIPTION_KEY="<content-moderator-key>"
export CONTENT_MODERATOR_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Run a dry check without calling Azure:

```bash
python tools/metadata/content_moderator.py \
  --input tools/translation/examples/sample_main.csv \
  --output outputs/metadata/sample_content_moderator.csv \
  --dry-run
```

Run the real job:

```bash
python tools/metadata/content_moderator.py \
  --input data/DSTC_11_Track_4/metadata/train/en/DAILYD/DAILYD_main.csv \
  --output outputs/metadata/DAILYD_content_moderator.csv \
  --yes
```

## Sentiment Analytics

Credentials are read from environment variables:

```bash
export TEXT_ANALYTICS_SUBSCRIPTION_KEY="<text-analytics-key>"
export TEXT_ANALYTICS_ENDPOINT="https://<resource>.cognitiveservices.azure.com/"
```

Common Azure aliases are also accepted: `AZURE_TEXT_ANALYTICS_KEY`, `AZURE_TEXT_ANALYTICS_ENDPOINT`, `LANGUAGE_KEY`, and `LANGUAGE_ENDPOINT`.

Run a dry check without calling Azure:

```bash
python tools/metadata/sentiment_analytics.py \
  --input tools/translation/examples/sample_main.csv \
  --utterance-output outputs/metadata/sample_utterance_sentiment_analytics.csv \
  --sentence-output outputs/metadata/sample_sentence_sentiment_analytics.csv \
  --dry-run
```

Both scripts write checkpoint CSV files under a local `records/` directory next to the output files. Use `--resume` to reuse existing checkpoints.

Never place real Azure keys in notebooks, command examples, Git history, or committed config files.
