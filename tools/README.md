# Tools

This directory contains the lightweight, publishable utilities used around DSTC11 Track 4.

## Setup

Install the shared lightweight Python dependencies before running translation or CSV utilities:

```bash
python -m pip install -r tools/requirements.txt
```

MTQE and paraphrase similarity use sentence-transformer models and have their own optional dependencies:

```bash
python -m pip install -r tools/mtqe/requirements.txt
python -m pip install -r tools/paraphrase/requirements.txt
```

Paraphrase generation also requires Parrot or the local `Parrot_Paraphraser/` snapshot, which is kept out of Git.

Azure-derived metadata regeneration has extra optional dependencies:

```bash
python -m pip install -r tools/metadata/requirements.txt
```

## Public Utilities

`translation/translate_text.py` translates CSV text columns with Azure Translator using credentials from environment variables.

`metadata/content_moderator.py` regenerates Content Moderator metadata using Azure credentials from environment variables.

`metadata/sentiment_analytics.py` regenerates utterance-level and sentence-level sentiment metadata using Azure credentials from environment variables.

`mtqe/compute_translation_similarity.py` computes sentence-embedding similarity scores for source, translation, and backtranslation columns.

`paraphrase/generate_paraphrases.py` generates paraphrases with an installed Parrot package or the local ignored Parrot snapshot.

`paraphrase/compute_paraphrase_similarity.py` computes similarity scores between source turns and generated paraphrases.

See [../docs/data-and-regeneration.md](../docs/data-and-regeneration.md) for the recommended workflow to download the dataset from Hugging Face and regenerate derived scores locally.

## Local-Only Material

Historical notebooks, old ad-hoc scripts, generated data, logs, pricing spreadsheets, virtual environments, MTQE data caches, and the local Parrot snapshot are ignored by Git. They are useful for local provenance, not for publication.
