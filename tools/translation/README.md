# Translation Tool

`translate_text.py` translates a CSV text column with Azure Translator.

Credentials are read from environment variables:

```bash
export TRANSLATOR_TEXT_SUBSCRIPTION_KEY="<translator-key>"
export TRANSLATOR_TEXT_ENDPOINT="https://api.cognitive.microsofttranslator.com/"
export TRANSLATOR_TEXT_REGION="westeurope"
```

`examples/sample_input.csv` is a minimal input file. It contains the source text
to translate, but not the translated output yet.

Example:

```bash
python tools/translation/translate_text.py \
  --csv-path tools/translation/examples/sample_input.csv \
  --save-path outputs/sample_translation_en_es.csv \
  --from-language en \
  --to-language es \
  --rows-per-checkpoint 50 \
  --batch-size 10 \
  --yes
```

An example translated output is available at:

```text
tools/translation/examples/sample_translation_en_es.csv
```

Use `--dry-run` to inspect the planned job without calling Azure.

Historical notebooks are not part of the public repository because executed notebooks can contain old credentials or personal paths.
