# Task 1: Metrics for Multilingual Data

In this task, the goal for participants is to propose effective automatic dialogue evaluation metrics that exhibit previously mentioned properties (section 2) and perform well on a multilingual setup (English, Spanish and Chinese). In concrete, participants will propose a single multilingual model obtaining high correlations with human-annotations when evaluated on multilingual dialogues (development set in section 2.1) and perform well on the hidden multilingual test set. Participants are expected to use pre-trained multilingual models and train them to predict multidimensional quality metrics by using self-supervised techniques and optionally fine-tune their system over a subset of the development data.

Finally, participants will then evaluate their models over the development and test sets, and expect to show similar performance, in terms of correlations with human-annotations on the English, Spanish and Chinese utterances. (Note: only dev and test sets will have human-annotations, and only test sets will be manually translated or back-translated/paraphrased to guarantee the correlations with the original human-annotations on the English data).

# Data Structure

The data in this directory is designed for Task 1 models. The data is divided into three directories: train, dev and test. In a first step of DSTC11, only the train and dev folders are available to the participants. The train data is separeted in different folders, depending the languages that contains.

*   en_es: original English sentences translated with MS Azure into Spanish.
*   en_zh: original English sentences translated into Chinese with a SotA Tencent MT system.
*   zh_en: original Chinese sentences translated into English with a SotA Tencent MT system.

# Translation Files Format

Translation for each turn from one language to another. The original English turns were automatically translated into Spanish and Chinese. For the Spanish translation, the [MS Azure](https://azure.microsoft.com/en-us/products/cognitive-services/translator/) service was used. An SotA [Tencent MT](https://www.tencentcloud.com/products/tmt) system was used for the Chinese translation.

**Naming Convention**: All files are named with the same structure as <dataset_id>_multilingual_<original_language>_<target_language>.csv.

**Index and attributes**: All Task 1 files have the same number of columns:

*	UID: the unique utterance indexes. Have three parts, dataset_id-dialog_id-turn_id.
*	SID: the speaker ids for each turn.
*	SEG: turn sentence in the original language.
*   TRANSLATION: translation of the SEG column from English to the target language.
*   COMET_20_ST: Quality estimator score between the SEG and TRANSLATION columns generated with the COMET 2020 model for each turn.
*   COMET_21_ST: Quality estimator score between the SEG and TRANSLATION columns generated with the COMET 2021 model for each turn.
*   COMET_22_ST: Quality estimator score between the SEG and TRANSLATION columns generated with the COMET 2022 model for each turn.
*   COS_SIM_MULTI_1_ST: Consine similarity between SEG and TRANSLATION columns for each turn. The term MULTI refers to multilinguality and the number 1 to a specific multilingual model.
*   COS_SIM_MULTI_2_ST: Consine similarity between SEG and TRANSLATION columns for each turn. The term MULTI refers to multilinguality and the number 2 to a specific multilingual model.

# MT Scores

[COMET](https://github.com/Unbabel/COMET) is a PyTorch-based framework for training highly multilingual and adaptable MT evaluation models that can function as metrics. It takes advantage of the cross-lingual encoder XLM-RoBERTa to generate prediction estimates of human judgments of Translation Quality such as *Direct Assessments* (DA), *Human-mediated Translation Edit Rate* (HTER) and metrics compliant with the *Multidimensional Quality Metric* framework.

Most COMET models are trained to regress on a specific quality assessment and in most cases the quality scores are normalised to obtain a z-score. This means that theoretically COMET models are unbounded. The score itself has no direct interpretation but they correctly rank translations and systems according to their quality.

Additional FAQ are available here: https://unbabel.github.io/COMET/html/faqs.html

## Scoring with Python 

Since there are no references, the translations should be scored using a QE (Quality Estimation) model.

## Available QE Models

[WMT20](https://aclanthology.org/2020.wmt-1.101/):&nbsp; `wmt20-comet-qe-da-v2`

[WMT21](https://aclanthology.org/2021.wmt-1.111):&nbsp; `wmt21-comet-qe-mqm`

[WMT22](https://arxiv.org/pdf/2209.06243.pdf):&nbsp; available soon

```
from comet import download_model, load_from_checkpoint

model_path = download_model("wmt20-comet-qe-da-v2")
model = load_from_checkpoint(model_path)

data =  [{"src":x,"mt":y} for x,y in zip(data.source,data.mt)]

seg_scores,_ = model.predict(data, batch_size=16, gpus=1)
```

# Cosine Similarity

To calculate cosine similarity, sentence embeddings were generated using the [SentenceTransformer](https://www.sbert.net/) library. For the columns COS_SIM_MULTI_1_ST and COS_SIM_MULTI_2_ST the multilingual models used are `distiluse-base-multilingual-cased-v1` and `paraphrase-xlm-r-multilingual-v1`, respectively. The cosine similarity was then calculated using the formula:

```math
CosineSimilarity(x, y) = 1 - CosineDistance(x, y)
```

```math
CosineSimilarity(x, y) = 1 - CosineDistance(x, y)
```

Find below an easy example of how to perform the Cosine Similarity on one turn for the Task 1 data.

```
import pandas as pd
from scipy.spatial import distance
from sentence_transformers import SentenceTransformer

data = pd.read_csv(path_dataset)

model_1_multi = SentenceTransformer('distiluse-base-multilingual-cased-v1')
model_2_multi = SentenceTransformer('paraphrase-xlm-r-multilingual-v1')

emb_seg_model_1_multi = model_1_multi.encode(data['SEG'][0])
emb_seg_model_2_multi = model_2_multi.encode(data['SEG'][0])
emb_tra_model_1_multi = model_1_multi.encode(data['TRANSLATION'][0])
emb_tra_model_2_multi = model_2_multi.encode(data['TRANSLATION'][0])

cos_similarity_model_1_multi_st = (1-distance.cosine(emb_seg_model_1_multi, emb_tra_model_1_multi))
cos_similarity_model_2_multi_st = (1-distance.cosine(emb_seg_model_2_multi, emb_tra_model_2_multi))
```