---
language:
- en
- zh
- es
tags:
- robust
- multilingual
- open-domain
pretty_name: >-
  DSTC11: Dialogue System Technology Challenge 11 Track 4: Robust and
  Multilingual Automatic Evaluation Metrics for Open-Domain Dialogue Systems
license: apache-2.0
configs:
- config_name: task1_train
  default: true
  data_files:
  - split: train
    path:
    - "DSTC_11_Track_4/task1/train/en_es/0DBDC3_multilingual_en_es.csv"
    - "DSTC_11_Track_4/task1/train/en_es/CMUDOG_multilingual_en_es.csv"
    - "DSTC_11_Track_4/task1/train/en_es/CORMOV_multilingual_en_es.csv"
    - "DSTC_11_Track_4/task1/train/en_es/DECODE_multilingual_en_es.csv"
    - "DSTC_11_Track_4/task1/train/en_es/ELINES_multilingual_en_es.csv"
    - "DSTC_11_Track_4/task1/train/en_es/HOLLED_multilingual_en_es.csv"
    - "DSTC_11_Track_4/task1/train/en_es/MEENAD_multilingual_en_es.csv"
    - "DSTC_11_Track_4/task1/train/en_es/MELDME_multilingual_en_es.csv"
    - "DSTC_11_Track_4/task1/train/en_es/METALW_multilingual_en_es.csv"
    - "DSTC_11_Track_4/task1/train/en_es/MOVDIC_multilingual_en_es.csv"
    - "DSTC_11_Track_4/task1/train/en_es/MPATHY_multilingual_en_es.csv"
    - "DSTC_11_Track_4/task1/train/en_es/PERCHT_multilingual_en_es.csv"
    - "DSTC_11_Track_4/task1/train/en_es/STLIAR_multilingual_en_es.csv"
    - "DSTC_11_Track_4/task1/train/en_es/SWBCOH_multilingual_en_es.csv"
    - "DSTC_11_Track_4/task1/train/en_es/TPCCHT_multilingual_en_es.csv"
    - "DSTC_11_Track_4/task1/train/en_es/WOCHAT_multilingual_en_es.csv"
    - "DSTC_11_Track_4/task1/train/en_es/WOWIKI_multilingual_en_es.csv"
    - "DSTC_11_Track_4/task1/train/en_zh/*.csv"
- config_name: task1_train_zh_en
  data_files:
  - split: train
    path:
    - "DSTC_11_Track_4/task1/train/zh_en/*.csv"
- config_name: task1_train_dailyd_backtranslation
  data_files:
  - split: train
    path: "DSTC_11_Track_4/task1/train/en_es/DAILYD_multilingual_en_es.csv"
- config_name: task1_dev
  data_files:
  - split: validation
    path:
    - "DSTC_11_Track_4/task1/dev/en_es/*.csv"
    - "DSTC_11_Track_4/task1/dev/en_zh/*.csv"
    - "DSTC_11_Track_4/task1/dev/zh_en/*.csv"
- config_name: task2_train
  data_files:
  - split: train
    path:
    - "DSTC_11_Track_4/task2/train/CMUDOG_paraphrases.csv"
    - "DSTC_11_Track_4/task2/train/ELINES_paraphrases.csv"
    - "DSTC_11_Track_4/task2/train/MEENAD_paraphrases.csv"
    - "DSTC_11_Track_4/task2/train/METALW_paraphrases.csv"
    - "DSTC_11_Track_4/task2/train/MPATHY_paraphrases.csv"
    - "DSTC_11_Track_4/task2/train/PERCHT_paraphrases.csv"
    - "DSTC_11_Track_4/task2/train/STLIAR_paraphrases.csv"
    - "DSTC_11_Track_4/task2/train/SWBCOH_paraphrases.csv"
    - "DSTC_11_Track_4/task2/train/TPCCHT_paraphrases.csv"
    - "DSTC_11_Track_4/task2/train/WOCHAT_paraphrases.csv"
- config_name: task2_train_similarity_legacy
  data_files:
  - split: train
    path:
    - "DSTC_11_Track_4/task2/train/DAILYD_paraphrases.csv"
    - "DSTC_11_Track_4/task2/train/MELDME_paraphrases.csv"
- config_name: task2_dev
  data_files:
  - split: validation
    path: "DSTC_11_Track_4/task2/dev/*.csv"
- config_name: metadata_main
  data_files:
  - split: train
    path: "DSTC_11_Track_4/metadata/train/**/*_main.csv"
  - split: validation
    path: "DSTC_11_Track_4/metadata/dev/**/*_main.csv"
- config_name: metadata_content_moderator_score_categories
  data_files:
  - split: train
    path:
    - "DSTC_11_Track_4/metadata/train/en/CMUDOG/CMUDOG_content_moderator.csv"
    - "DSTC_11_Track_4/metadata/train/en/DECODE/DECODE_content_moderator.csv"
    - "DSTC_11_Track_4/metadata/train/en/HOLLED/HOLLED_content_moderator.csv"
    - "DSTC_11_Track_4/metadata/train/en/METALW/METALW_content_moderator.csv"
    - "DSTC_11_Track_4/metadata/train/en/MOVDIC/MOVDIC_content_moderator.csv"
    - "DSTC_11_Track_4/metadata/train/en/TPCCHT/TPCCHT_content_moderator.csv"
    - "DSTC_11_Track_4/metadata/train/en/WOWIKI/WOWIKI_content_moderator.csv"
  - split: validation
    path: "DSTC_11_Track_4/metadata/dev/**/*_content_moderator.csv"
- config_name: metadata_content_moderator_profanity_scores
  data_files:
  - split: train
    path:
    - "DSTC_11_Track_4/metadata/train/en/0DBDC3/0DBDC3_content_moderator.csv"
    - "DSTC_11_Track_4/metadata/train/en/CORMOV/CORMOV_content_moderator.csv"
    - "DSTC_11_Track_4/metadata/train/en/DAILYD/DAILYD_content_moderator.csv"
    - "DSTC_11_Track_4/metadata/train/en/ELINES/ELINES_content_moderator.csv"
    - "DSTC_11_Track_4/metadata/train/en/MEENAD/MEENAD_content_moderator.csv"
    - "DSTC_11_Track_4/metadata/train/en/MELDME/MELDME_content_moderator.csv"
    - "DSTC_11_Track_4/metadata/train/en/MPATHY/MPATHY_content_moderator.csv"
    - "DSTC_11_Track_4/metadata/train/en/PERCHT/PERCHT_content_moderator.csv"
    - "DSTC_11_Track_4/metadata/train/en/STLIAR/STLIAR_content_moderator.csv"
    - "DSTC_11_Track_4/metadata/train/en/SWBCOH/SWBCOH_content_moderator.csv"
    - "DSTC_11_Track_4/metadata/train/en/WOCHAT/WOCHAT_content_moderator.csv"
- config_name: metadata_utterance_sentiment
  data_files:
  - split: train
    path: "DSTC_11_Track_4/metadata/train/**/*_utterance_sentiment_analytics.csv"
  - split: validation
    path: "DSTC_11_Track_4/metadata/dev/**/*_utterance_sentiment_analytics.csv"
- config_name: metadata_sentence_sentiment_idx
  data_files:
  - split: train
    path:
    - "DSTC_11_Track_4/metadata/train/en/CMUDOG/CMUDOG_sentence_sentiment_analytics.csv"
    - "DSTC_11_Track_4/metadata/train/en/DECODE/DECODE_sentence_sentiment_analytics.csv"
    - "DSTC_11_Track_4/metadata/train/en/HOLLED/HOLLED_sentence_sentiment_analytics.csv"
    - "DSTC_11_Track_4/metadata/train/en/METALW/METALW_sentence_sentiment_analytics.csv"
    - "DSTC_11_Track_4/metadata/train/en/MOVDIC/MOVDIC_sentence_sentiment_analytics.csv"
    - "DSTC_11_Track_4/metadata/train/en/TPCCHT/TPCCHT_sentence_sentiment_analytics.csv"
    - "DSTC_11_Track_4/metadata/train/en/WOWIKI/WOWIKI_sentence_sentiment_analytics.csv"
  - split: validation
    path: "DSTC_11_Track_4/metadata/dev/**/*_sentence_sentiment_analytics.csv"
- config_name: metadata_sentence_sentiment_sentence_idx
  data_files:
  - split: train
    path:
    - "DSTC_11_Track_4/metadata/train/en/0DBDC3/0DBDC3_sentence_sentiment_analytics.csv"
    - "DSTC_11_Track_4/metadata/train/en/CORMOV/CORMOV_sentence_sentiment_analytics.csv"
    - "DSTC_11_Track_4/metadata/train/en/DAILYD/DAILYD_sentence_sentiment_analytics.csv"
    - "DSTC_11_Track_4/metadata/train/en/ELINES/ELINES_sentence_sentiment_analytics.csv"
    - "DSTC_11_Track_4/metadata/train/en/MEENAD/MEENAD_sentence_sentiment_analytics.csv"
    - "DSTC_11_Track_4/metadata/train/en/MELDME/MELDME_sentence_sentiment_analytics.csv"
    - "DSTC_11_Track_4/metadata/train/en/MPATHY/MPATHY_sentence_sentiment_analytics.csv"
    - "DSTC_11_Track_4/metadata/train/en/PERCHT/PERCHT_sentence_sentiment_analytics.csv"
    - "DSTC_11_Track_4/metadata/train/en/STLIAR/STLIAR_sentence_sentiment_analytics.csv"
    - "DSTC_11_Track_4/metadata/train/en/SWBCOH/SWBCOH_sentence_sentiment_analytics.csv"
    - "DSTC_11_Track_4/metadata/train/en/WOCHAT/WOCHAT_sentence_sentiment_analytics.csv"
---

# DSTC11: Dialogue System Technology Challenge 11

## [Track 4: Robust and Multilingual Automatic Evaluation Metrics for Open-Domain Dialogue Systems](https://github.com/Mario-RC/dstc11_track4_robust_multilingual_metrics)

This public dataset release contains multilingual and robustness data for building and evaluating automatic metrics for open-domain dialogue systems. It includes public train and development data, public evaluation templates, and auxiliary metadata. Held-out test data is not included in this public Hugging Face release.

GitHub repository: [Mario-RC/dstc11_track4_robust_multilingual_metrics](https://github.com/Mario-RC/dstc11_track4_robust_multilingual_metrics)

## Dataset Structure

Representation of the public release directory tree:

```text
.
└── DSTC_11_Track_4             # DSTC11 Track 4 public data
    ├── eval                    # Public evaluation and submission templates
    │   ├── task1               # Task 1 evaluation templates
    │   └── task2               # Task 2 evaluation templates
    ├── task1                   # Multilingual metrics data
    │   ├── train               # Train data (CHANEL/CDial datasets)
    │   │   ├── en_es           # English/Spanish data
    │   │   ├── en_zh           # English/Chinese data
    │   │   └── zh_en           # Chinese/English data
    │   ├── dev                 # Development data (DSTC10.T5/CDial datasets)
    │   │   ├── en_es           # English/Spanish data
    │   │   ├── en_zh           # English/Chinese data
    │   │   └── zh_en           # Chinese/English data
    │   └── README.md           # Task 1 data information
    ├── task2                   # Robust metrics data
    │   ├── train               # Train data (CHANEL datasets)
    │   ├── dev                 # Development data (DSTC10.T5 datasets)
    │   └── README.md           # Task 2 data information
    ├── metadata                # Auxiliary dataset annotations
    │   ├── train               # Train metadata
    │   └── dev                 # Development metadata
    └── README.md               # General data information
```

Task 1 is organized by language direction:

```text
task1/{train,dev}/en_es/
task1/{train,dev}/en_zh/
task1/{train,dev}/zh_en/
```

Task 2 is organized by source dataset and contains paraphrase/backtranslation variants.

## Release Contents

| Area | Contents |
| --- | --- |
| `DSTC_11_Track_4/task1/train/` | Multilingual training data from English and Chinese dialogue corpora |
| `DSTC_11_Track_4/task1/dev/` | Multilingual development data with human-evaluation targets |
| `DSTC_11_Track_4/task2/train/` | Robustness training data with paraphrases and backtranslations |
| `DSTC_11_Track_4/task2/dev/` | Robustness development data with human-evaluation targets |
| `DSTC_11_Track_4/metadata/train/` | Auxiliary train metadata, including moderation and sentiment files |
| `DSTC_11_Track_4/metadata/dev/` | Auxiliary development metadata |
| `DSTC_11_Track_4/eval/` | Public evaluation and submission-template CSV files |

## Not Included

The held-out test data used by the DSTC11 Track 4 organizers is intentionally not part of this public release. In particular, this release does not include:

```text
DSTC_11_Track_4/task1/test/
DSTC_11_Track_4/task2/test/
DSTC_11_Track_4/metadata/test/
```

If held-out test data is needed for research or evaluation, request access from the DSTC11 Track 4 organizers through the contact information in the GitHub repository.

## Download

Download the full public release with `huggingface_hub`:

```python
from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="mario-rc/dstc11.t4",
    repo_type="dataset",
    allow_patterns=["DSTC_11_Track_4/**"],
    local_dir="data",
)
```

## Data Fields

The exact columns depend on the subset. Common fields include:

| Field | Meaning |
| --- | --- |
| `UID` | Utterance-level identifier |
| `SID` | Source dialogue or sample identifier, when available |
| `DID` | Dialogue-level identifier, when available |
| `SEG` | Source segment or utterance text |
| `TRANSLATION` | Machine-translated segment |
| `BACKTRANSLATION` | Backtranslated segment |
| `PARAPHRASES` | Generated paraphrase text |
| `COMET_*` | Machine-translation quality-estimation scores |
| `COS_SIM_*` | Sentence-similarity scores for translation, backtranslation, or paraphrase pairs |
| `LEVENSHTEIN` | String-distance score for paraphrase variants |
| `profanity_terms` | Terms flagged by moderation metadata |
| `*_score` | Moderation, sentiment, or evaluation score columns |

## Tasks

**Task 1: Multilingual Automatic Evaluation Metrics**

Task 1 supports research on automatic dialogue evaluation metrics that transfer across English, Spanish, and Chinese. The data includes multilingual translations and development annotations for measuring correlation with human judgements.

**Task 2: Robust Automatic Evaluation Metrics**

Task 2 supports research on robustness to paraphrased and backtranslated responses in English. The data includes paraphrase variants and similarity features intended for stress-testing dialogue-evaluation metrics.

For both tasks, submitted metrics are evaluated by correlation with human judgements, including turn-level and dialogue-level dimensions.

## Evaluation Dimensions

Turn-level dimensions:

- Appropriateness
- Content richness
- Grammatical correctness
- Relevance

Dialogue-level dimensions:

- Coherence
- Engageness/likeability
- Informativeness
- Overall quality

Evaluation templates in `DSTC_11_Track_4/eval/` may contain empty target columns by design. They are intended for submission formatting and are not training labels.

## Source Collections

The release builds on public and challenge datasets used in DSTC11 Track 4, including:

- CHANEL/JSALT-derived English dialogue corpora used for training data
- DSTC10 Track 5 dialogue-evaluation data used for development data
- CDial Chinese dialogue corpora from THU-CoAI
- Chinese human-chatbot and human-human annotation data contributed during the track

The training data covers 18 English dialogue corpora translated into Spanish and Chinese, plus Chinese corpora translated into English. Development data includes multilingual versions of DSTC10 Track 5 evaluation datasets.

## Further Documentation

- [Provided datasets](https://github.com/Mario-RC/dstc11_track4_robust_multilingual_metrics/blob/main/dstc11/track4-provided-datasets.md)
- [Datasets format](https://github.com/Mario-RC/dstc11_track4_robust_multilingual_metrics/blob/main/dstc11/track4-datasets-format.md)
- [Task 1: Multilingual Automatic Evaluation Metrics](https://github.com/Mario-RC/dstc11_track4_robust_multilingual_metrics/blob/main/dstc11/track4-task1-metrics-multilingual-data.md)
- [Task 2: Robust Automatic Evaluation Metrics](https://github.com/Mario-RC/dstc11_track4_robust_multilingual_metrics/blob/main/dstc11/track4-task2-robust-metrics.md)

## Licensing

The dataset repository is released under the Apache 2.0 license. Users should also respect the licenses and usage terms of the underlying source datasets referenced by DSTC11 Track 4.

## Organizers

- Mario Rodríguez-Cantelar, Universidad Politécnica de Madrid, Spain
- Chen Zhang, National University of Singapore, Singapore
- Chengguang Tang, Tencent AI Lab, China
- Ke Shi, Tencent AI Lab, China
- Sarik Ghazarian, University of Southern California, USA
- João Sedoc, New York University, USA
- Luis F. D'Haro, Universidad Politécnica de Madrid, Spain
- Alexander Rudnicky, Carnegie Mellon University, USA

## Citation

Please cite the DSTC11 Track 4 overview paper when using this dataset:

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

## Acknowledgements

This research project was supported by Comunidad de Madrid, Universidad Politécnica de Madrid, project BEWORD, Tencent AI Lab, THU-CoAI, Unbabel, MS Azure services, the NYU ChatEval Team, Amazon support to Carnegie Mellon University, and the European Commission through Project ASTOUND.

The organizers thank all contributors involved in dataset preparation, translation, annotation, baseline development, and evaluation infrastructure for DSTC11 Track 4.
