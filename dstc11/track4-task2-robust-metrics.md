# Task 2: Robust Metrics

In this task, the goal for participants is to propose robust metrics for automatic evaluation of just English dialogues that exhibit previously mentioned properties (section 2) while being robust when dealing with back-translated/paraphrased English sentences. The expected performance must be on par with the correlations with human-annotations obtained over the original sentences. As robustness criteria proposed, back-translated/paraphrased sentences should have the same semantic meaning as the original sentence, but different wording.

Additionally, participants will have the opportunity of testing robustness over alternative machine translations that the organizers will provide. Finally, the influence on the metric will be also evaluated when providing the back-translated/paraphrased current turn sentences instead of the original ones, always along with their respective back-translated/paraphrased context.

During the test phase, hidden and manually curated back-translated test data will be provided to participants to evaluate their proposed metrics.

# Data Structure

The data in this directory is designed for Task 2 models. The data is divided into three directories: train, dev and test. In a first step of DSTC11, only the train and dev folders are available to the participants.

# Paraphrases and Back-translation Files Format

On the one hand, there are the paraphrases of each turn from the original turn. On the other hand, there is the back-translation of the turn translated into Spanish used for Task 1.

**Naming Convention**: All files are named with the same structure as <dataset-id>_paraphrases.csv.

**Index and attributes**: All Task 2 files have the same number of columns:

*	UID: the unique utterance indexes. Have three parts, dataset_id-dialog_id-turn_id.
*	SID: the speaker ids for each turn.
*	SEG: turn sentence in the original language.
*   PARAPHRASES: paraphrase of the SEG column. Each turn contains a different number of paraphrases in a list of strings.
*   LEVENSHTEIN: distance from each paraphrase to the SEG. The scores in the list correspond respectively to the list of strings in the PARAPHRASIS column.
*   COS_SIM_MONO_SP: Consine similarity between the SEG and PARAPHRASIS columns of each turn. MONO refers to monolinguality.
*   BACKTRANSLATION: back-translation of the TRANSLATION column from Spanish to English, performed for Task 1.
*   COS_SIM_MONO_SB: Consine similarity between the SEG and BACKTRANSLATION columns of each turn. MONO refers to monolinguality.

## Paraphrases

[PARROT](https://github.com/jsedoc/Parrot_Paraphraser/blob/main/parrot/paraphrase.py) is a paraphrase based utterance augmentation framework purpose built to accelerate training NLU models.

Each turn has multiple paraphrases generated with the `prithivida/parrot_parrot_paraphraser_on_T5` model. The model returns a different number of paraphrases depending on the phrase entered, as well as the levenshtein metric for each paraphrase. In case the model did not generate any paraphrases, the csv cell will contain a *None* string. In this case, back-translation is also a good option. In any case, the participant is free to decide what to do, use external methods, suppress the turn, suppress the dialog, etc.

To run the Parrot library with the setting used in DSTC11, follow the steps below: https://github.com/jsedoc/Parrot_Paraphraser.

To correctly read the list of strings in the PARAPHRASIS column of each csv, use the following command lines:
```
import pandas as pd
import ast

data = pd.read_csv(path_dataset)
data['PARAPHRASES'] = data['PARAPHRASES'].apply(ast.literal_eval)
```

## Back-translation

The original English turns were automatically translated into Spanish for Task 1. Then, for this Task 2, the Spanish translation was back-translated into English using the same multilingual models as for the translation, the [MS Azure](https://azure.microsoft.com/en-us/products/cognitive-services/translator/) service.

# Cosine Similarity

To calculate cosine similarity, sentence embeddings were generated using the [SentenceTransformer](https://www.sbert.net/) library. For the columns COS_SIM_MONO_SP and COS_SIM_MONO_SB the monolingual model used is `paraphrase-TinyBERT-L6-v2`. The cosine similarity was then calculated using the formula:

```math
CosineSimilarity(x, y) = 1 - CosineDistance(x, y)
```

Find below an easy example of how to perform the Cosine Similarity on one turn for the Task 2 data.

```
import pandas as pd
import ast
from scipy.spatial import distance
from sentence_transformers import SentenceTransformer

model_1_mono = SentenceTransformer('paraphrase-TinyBERT-L6-v2')

data = pd.read_csv(path_dataset)
data['PARAPHRASES'] = data['PARAPHRASES'].apply(ast.literal_eval)

emb_seg_model_1_mono = model_1_mono.encode(data['SEG'][0])
emb_par_model_1_mono = model_1_mono.encode(data['PARAPHRASES'][0][0])
emb_bac_model_1_mono = model_1_mono.encode(data['BACKTRANSLATION'][0])

cos_similarity_model_1_multi_st = (1-distance.cosine(emb_seg_model_1_mono, emb_par_model_1_mono))
cos_similarity_model_2_multi_sb = (1-distance.cosine(emb_seg_model_1_mono, emb_bac_model_1_mono))
```