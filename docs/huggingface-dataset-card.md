---
language:
- en
- zh
- es
tags:
- robust
- multilingual
- open-domain
- dialogue-evaluation
pretty_name: >-
  DSTC11 Track 4: Robust and Multilingual Automatic Evaluation Metrics for
  Open-Domain Dialogue Systems
license: apache-2.0
viewer: false
---

# DSTC11 Track 4

Public dataset release for DSTC11 Track 4: Robust and Multilingual Automatic Evaluation Metrics for Open-Domain Dialogue Systems.

GitHub repository:

```text
https://github.com/Mario-RC/dstc11_track4_robust_multilingual_metrics
```

## Files

The dataset is distributed as a compressed archive:

```text
DSTC_11_Track_4.zip
```

Download and extract it locally before use.

## Public Release Contents

This Hugging Face release is intended for the public train/development data and related documentation. Held-out test data is intentionally not included in the public archive.

If test data is needed for research or evaluation, request access from the DSTC11 Track 4 organizers through the contact address listed in the GitHub repository.

## Local Layout

After extraction, place the dataset under:

```text
data/DSTC_11_Track_4/
```

Expected public data areas:

```text
DSTC_11_Track_4/
├── task1/
│   ├── train/
│   └── dev/
├── task2/
│   ├── train/
│   └── dev/
├── metadata/        # optional auxiliary metadata; no held-out test files
└── README.md
```

Additional documentation is available in the GitHub repository.

## Usage Notes

Large data files should not be committed to GitHub. Use the Hugging Face archive for dataset distribution and the GitHub repository for documentation and reusable scripts.

Derived MTQE and paraphrase similarity scores can be regenerated locally from the public data using the scripts in the GitHub repository:

```text
tools/mtqe/compute_translation_similarity.py
tools/paraphrase/compute_paraphrase_similarity.py
```

Azure-derived moderation and sentiment metadata can also be regenerated with the optional metadata tools:

```text
tools/metadata/content_moderator.py
tools/metadata/sentiment_analytics.py
```

Regenerating original translations, backtranslations, moderation metadata, or sentiment metadata from raw text may require external paid services. Normal users should use the released archive instead of re-running paid service jobs.

## Citation

```bibtex
@inproceedings{rodriguezcantelar2023dstc11t4,
    author    = "Mario Rodríguez-Cantelar and Chen Zhang and Chengguang Tang and Ke Shi and Sarik Ghazarian and João Sedoc and Luis Fernando D'Haro and Alexander Rudnicky",
    title     = "Overview of Robust and Multilingual Automatic Evaluation Metrics for Open-Domain Dialogue Systems at DSTC 11 Track 4",
    booktitle = "DSTC11: The Eleventh Dialog System Technology Challenge",
    series    = "24th Meeting of the Special Interest Group on Discourse and Dialogue (SIGDIAL)",
    year      = 2023,
    month     = "September",
    address   = "Prague, Czechia"
}
```
