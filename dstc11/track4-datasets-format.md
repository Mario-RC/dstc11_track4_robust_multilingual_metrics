# Datasets Fornat

## Directory Structure Scheme

Representation of the directory tree structure:
```
.
└── DSTC_11_Track_4             # DSTC11 data
    ├── task1                   # Metrics for Multilingual Data data
    │       ├── train           # Train data (JSALT2020 datasets)
    │       │   ├── en_es       # English/Spanish data
    │       │   ├── en_zh       # English/Chinese data
    │       │   └── zh_en       # Chinese/English data
    │       ├── dev             # Dev data (DSTC10.T5 datasets)
    │       │   ├── en_es       # English/Spanish data
    │       │   └── en_zh       # English/Chinese data
    │       ├── test            # Test data (DSTC10.T5 datasets)
    │       │   ├── en_es       # English/Spanish data
    │       │   └── en_zh       # English/Chinese data
    │       └── README.md       # Task 1 data information
    ├── task2                   # Robust Metrics data
    │       ├── train           # Train data (JSALT2020 datasets)
    │       ├── dev             # Development data (DSTC10.T5 datasets)
    │       ├── test            # Test data (DSTC10.T5 datasets)
    │       └── README.md       # Task 2 data information
    ├── metadata                # Auxiliary datasets annotations
    └── README.md               # General data information
```

# [Unified Dialogue Data Formats](https://github.com/CHANEL-JSALT-2020/Wiki/wiki/Unified-Dialogue-Data-Formats)

Chanel Unified Dialogue Data Formats provides guidelines on how to store, maintain and handle dialogue corpora.

## Multiple File System

Dialogue datasets are stored across multiple files. This are the supported types of files:
*	**Readme**. A .txt file providing general information about the corpus.
*	**Translation and Back-translation**. Contains the translation of each utterance from the original source language to the target language and the back-translation into the original source language.
*	**Main**. The main data file of the corpus in .csv format containing the raw text of the turns and the main indexes.
*	**Context**. Used to provide dialogue context information at the turn and supra-turn level in .csv format.
*	**Dialoginfo**. Used to save information that is relevant at the dialogue level.
*	**Sentiment Analytics**. Include sentiment analysis annotations of each utterance/sentence.
*	**Content Moderator**. Include toxicity annotations of each utterance.

# [File Data Formats](https://github.com/CHANEL-JSALT-2020/Wiki/wiki/File-Data-Formats)

The main data file of a corpus is a .csv file containing the raw text of the turns and the main UID indexes.

## Translation and Back-translation File Format

Translate each utterance string from one language to another, and then back-translate from the translated language to the original language.

**Naming Convention**: the translation file must be named as "cccccc_main_<from_language>_<to_language>_<from_language>.csv", where cccccc is the corpus index CID.

**Index and attributes**: the translation file must contain at least three mandatory columns:
*	UID: the unique utterance indexes.
*	SID: the speaker names or ids for each turn.
*	SEG: the raw segment of text comprising the turn.
*	TRANSLATION: translation from one language to another.
*   BACKTRANSLATION: back-translation from the translated language to the original language.

## Main File Format

The main data file of a corpus is a .csv file containing the raw text of the turns and the main UID indexes.

The UID is of the form cccccc-dddddd-uuuu, where:
*	cccccc: six alphanumeric characters identifying the corpus.
*	dddddd: six digits identifying the dialogue number inside the corpus.
*	uuuu: four digits identifying the utterance number inside the dialogue.

**Naming Convention**: the main file must be named as "cccccc_main.csv", where cccccc is the corpus index CID.
*	CID (corpus index): cccccc the six alphanumeric characters identifying the corpus.

**Index and attributes**: the main file must contain at least three mandatory columns:
*	UID: the unique utterance indexes.
*	SID: the speaker names or ids for each turn.
*	SEG: the raw segment of text comprising the turn.

Full information in [Unified Dialogue Data Formats](https://github.com/CHANEL-JSALT-2020/Wiki/wiki/Unified-Dialogue-Data-Formats) and [File Data Formats](https://github.com/CHANEL-JSALT-2020/Wiki/wiki/File-Data-Formats).

## Context and Dialoginfo File Format

Auxiliary files providing complementary dialogue metadata related to the corpus.

Index and attributes: the context file must contain at least one mandatory column:
*	DID (dialogue index): cccccc-dddddd the CID followed by the dialogue number.

Full information in [Unified Dialogue Data Formats](https://github.com/CHANEL-JSALT-2020/Wiki/wiki/Unified-Dialogue-Data-Formats) and [File Data Formats](https://github.com/CHANEL-JSALT-2020/Wiki/wiki/File-Data-Formats).

## Sentiment Analysis File Format

The Text Analytics API is a cloud-based service that provides advanced natural language processing over raw text and includes the sentiment analysis function. The utterance contains the sentiment analysis of each dialogue. The sentence contains the sentiment analysis of each sentence per utterance.

**Naming Convention**: the sentiment analysis file must be named as "cccccc_{utterance/sentence}_sentiment_analytics.csv", where cccccc is the corpus index CID.

**Index and attributes**: the utterance sentiment analysis file must contain at least six mandatory columns:
*	UID: the unique utterance indexes.
*	SEG: the raw segment of text comprising the turn.
*	utt_sentiment: sentiment label of the entire utterance.
*	utt_pos_score: positive sentiment score of the entire utterance.
*	utt_neu_score: neutral sentiment score of the entire utterance.
*	utt_neg_score: negative sentiment score of the entire utterance.

**Index and attributes**: the sentence sentiment analysis file must contain at least seven mandatory columns:
*	SUID (sub-utternace index): cccccc-dddddd-uuuu-[xxxx,xxxx] the UID followed by the start and end character numbers.
*	sentence_split: the raw segment of text comprising the turn per utterance.
*	sentence_idx: the index of each sentence related to its utterance.
*	sentence_sentiment: sentiment analysis label for each sentence.
*	pos_score: positive sentiment analysis score for each sentence.
*	neu_score: neutral sentiment analysis score for each sentence.
*	neg_score: negative sentiment analysis score for each sentence.

## Content Moderator File Format

Content Moderator is a cognitive service that checks text content for material that is potentially offensive, risky, or otherwise undesirable.

**Naming Convention**: the content moderator file must be named as "cccccc_content_moderator.csv.csv", where cccccc is the corpus index CID.

**Index and attributes**: the content moderator file must contain at least seven mandatory columns:
*	UID: the unique utterance indexes.
*	SEG: the raw segment of text comprising the turn.
*	profanity_terms: profane terms detected.
*	sexually_explicit_adult_score: refers to potential presence of language that may be considered sexually explicit or adult in certain situations.
*	sexually_suggestive_mature_score: refers to potential presence of language that may be considered sexually suggestive or mature in certain situations.
*	offensive_score: refers to potential presence of language that may be considered offensive in certain situations.
*	review_recommended: is either true or false depending on the category scores.