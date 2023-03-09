# Provided Datasets

After the organizers' participation in the [CHANEL@JSALT2020](https://github.com/CHANEL-JSALT-2020/datasets) workshop (Rudnicky et al., 2020) at John Hopkins University, they have automatically translated back-and-forth (using the same MS Azure translation service) a total of 18 well-known human-human dialogue datasets. These data sets will be used as training data. The total amount of dialogues is 393k (approx. 3M turns).

* DBDC (Higashinaka et al., 2016)
* CMU_DoG (Zhou et al., 2018)
* Cornell Movie-Dialogs (Danescu-Niculescu-Mizil & Lee, 2011)
* DailyDialog (Li et al., 2017)
* DECODE (Nie et al., 2020)
* EmotionLines (Chen et al., 2018)
* EmpathicDialogues (Rashkin et al., 2018)
* Holl-E (Moghe et al., 2018)
* MEENA (Adiwardana et al., 2020)
* MELD (Poria et al., 2019)
* MetalWOz (Lee et al., 2019)
* Movie-DiC (Banchs, 2012)
* PersonaChat (Zhang et al., 2018)
* SentimentLIAR (Upadhayay & Behzadan, 2020)
* Switchboard Coherence (Cervone & Riccardi, 2020)
* Topical-Chat (Gopalakrishnan et al., 2019)
* Wizard of Wikipedia (Dinan et al., 2019)
* Wochat (D'Haro et al., 2016)

As development set, organizers will provide the following datasets identified during the [DSTC10 Track 5](https://chateval.org/dstc10) (Zhang et al, 2021), that sum up more than 35k turn-level human-annotations, which have been automatically translated to Spanish and Chinese, and back-translated both to English using [MS Azure](https://azure.microsoft.com/en-us/products/cognitive-services/translator/) services.

* CONVAI2-GRADE (CG)</b> (Huang et al., 2020)
* DAILYDIALOG-GRADE (DH)</b> (Huang et al., 2020)
* DAILYDIALOG-GUPTA (DG)</b> (Gupta et al., 2019)
* DAILYDIALOG-ZHAO (DZ)</b> (Zhao et al., 2020)
* DSTC7 (D7)</b> (Galley et al., 2019)
* EMPATHETIC-GRADE (EG)</b> (Huang et al., 2020)
* FED-DIAL (FD)</b> (Mehri & Eskenazi, 2020b)
* FED-TURN (FT)</b> (Mehri & Eskenazi, 2020b)
* HUMOD (HM)</b> (Merdivan et al., 2020)
* PERSONA-SEE (PS)</b> (See et al., 2019)
* PERSONA-USR (PU)</b> (Mehri & Eskenazi, 2020a)
* PERSONA-ZHAO (PZ)</b> (Zhao et al., 2020)
* TOPICAL-USR (TU)</b> (Mehri & Eskenazi, 2020a)

This development data can help participants to check the multilingualism or robustness capabilities of their trained models in terms of correlations with human-annotations. Additional databases, not mentioned here, will be added when available to increase the size of the benchmarking.

Moreover, the datasets provided by [THU-COAI](https://github.com/thu-coai) group (Conversational AI groups from Tsinghua University) will be used, naming this set of data CDial. They contain open domain human-human dialogs. They are originally in Chinese and contain of 3,470 dialogs (approx. 130k turns).

* ECM (Zhou et al., 2018)
* KdConv (Zhou et al., 2020)
* LCCC (Wang et al., 2020)

In addition, we will provide the same datasets translated (CHANEL@JSALT2020 and CDial) into Chinese using the SotA [Tencent MT](https://www.tencentcloud.com/products/tmt) system.

These datasets will be provided to participants, together with automatic meta-data information (machine translation Quality Estimation (QE), toxicity, and sentiment analysis) for filtering and dialogue curation purposes, so the participants have a better reference of the dataset quality, being of great help for them to decide whether or not to use these translations/paraphrases in the training of their evaluation models, and optionally fine-tune multilingual pre-trained models allowing better performance on the proposed dialogue-oriented tasks.

Since the quality of the back-translated sentences can play an important role in estimating the metric scores. QE metric scores will be given to the participants using our QE system and other existing models (e.g., [COMET](https://github.com/Unbabel/COMET) (Rei et al., 2020)). This information will be given to participants so they can optionally use it for discarding dialogues or turns that do not show high quality when training their metrics. Participants will be welcome to use the data and ideas from the MT field to propose QE metrics that can, optionally, be included to provide final scores. Finally, the organizers may provide new translated dialogue datasets to allow participants to create more robust and better-trained systems.

Regarding the paraphrases, all the original English sentences of each dataset will have multiple paraphrases, as well as annotations so that each participant can evaluate the quality of each paraphrase. The model used will be [PARROT](https://github.com/jsedoc/Parrot_Paraphraser) (Damodaran P., 2021).

Additionally, ~3k random H-H turns (~1k dialogues) of CDial in Chinese were manually annotated by Tencent AI. Also, ~5k new H-C Chinese turns (~500 dialogues) were generated with three different SotA chatbots (Tencent's model, Microsoft's Xiaoice (Zhou et al., 2020) and Baidu's Plato (Bao et al., 2019)). Both turn-level and dialog-level annotations were manually annotated by Tencent AI.

During the test phase, a new set of 2k turn-level (~700 dialog-level) manually curated multilingual corpus (Spanish and Chinese) along with their turn-level and dialog-level human evaluation annotations will be provided to participants to test models for both tasks. This corpus will be manually checked to guarantee its quality and high correlation with the original dialogues.

Furthermore, in order to check the generalization capabilities of the proposed metrics from the participant, the test data will include a new dataset of human-chatbot interactions with ~2k turns (~60 dialogues) and the following dimensions (annotations) to evaluate:

* Turn-level: Relevant, Appropriateness and Content Richness.
* Dialogue-level: Overall, Coherence and Likeability/Engageness.

# Datasets Summary

| Datasets<br/>Name | CHANEL | DSTC10 | CDIAL |
| --- | :---: | :----: | :---: |
| # Datsets | 18 | 7 | 3 |
| Language | English, Spanish/Chinese translations,<br/>and English back-translation | English, Spanish/Chinese translations,<br/>and English back-translation | Chinese and English translations |
| Dialogues Type | Human-Human Open-Domain | Human-Chatbot Open-Domain | Human-Human Open-Domain
| # Dialogues/<br/>Utterances | + 390.000 / + 3.000.000 | + 3.000 / + 60.000 | + 3.470 / +130.000
| Annotations | Sentiment analysis and Toxicity | Sentiment analysis and Toxicity<br/>Turn/dialgue level human scores | Turn/dialgue level human scores
| Task 1 Set | Train | Dev, Test | Train, Dev, Test
| Task 2 Set | Train | Dev, Test | —

<!-- # Datasets Statistics

| Dataset | No. Turns/Dialogues | No. Anno Qualities | No. Annos | AVG. Utts | AVG. Words per Utts |
| --- | --- | --- | --- | --- | --- |
| CONVAI2-GRADE (CG) | 300 | 1 | 3000 | 3.00 | 11.89 |
| DAILYDIALOG-GRADE (DH) | 300 | 1 | 3000 | 3.00 | 12.25 |
| DAILYDIALOG-GUPTA (DG) | 500 | 1 | 1500 | 4.92 | 12.36 |
| DAILYDIALOG-ZHAO (DZ) | 900 | 4 | 14400 | 4.72 | 12.39 |
| DSTC7 (D7) | 9900 | 1 | 29700 | 4.92 | 20.18 |
| EMPATHETIC-GRADE (EG) | 300 | 1 | 3000 | 3.00 | 14.86 |
| FED-DIAL (FD) | 125 | 11| 1364 | 12.72 | 8.70 |
| FED-TURN (FT) | 375  | 9 | 3348 | 10.37 | 9.70 |
| HUMOD (HM) | 9500 | 2 | 57000 | 3.95 | 4.31 |
| PERSONA-SEE (PS) | 3316 | 9 | 29844 | 12.00 | 7.59 |
| PERSONA-USR (PU) | 300 | 6 | 5400 | 9.30 | 11.87 |
| PERSONA-ZHAO (PZ) | 900 | 1 | 3600 | 5.13 | 11.77 |
| TOPICAL-USR (TU) | 360 | 6 | 6480 | 11.20 | 23.14 | -->

# Datasets Information

CHANEL dataset is Task 1 and Task 2 oriented. The source language is English.

| CHANEL | Spanish<br/>Translation | Chinese<br/>Translation | English<br/>Translation | English<br/>Back-translation | Paraphrases | Sentiment<br/>Analysis | Content<br/>Moderate | Human<br/>Annotations | Annotation<br/>Granularity |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| DBDC | ✔ | | | ✔ | ✔ | ✔ | ✔ | | Turn-level |
| CMU_DoG | ✔ | | | ✔ | ✔ | ✔ | ✔ | | Turn-level |
| Cornell Movie-Dialogs | ✔ | | | ✔ | ✔ | ✔ | ✔ | | Turn-level |
| DailyDialog | ✔ | ✔ | | ✔ | ✔ | ✔ | ✔ | | Turn-level |
| DECODE | ✔ | | | ✔ | ✔ | ✔ | ✔ | | Turn-level |
| EmotionLines | ✔ | | | ✔ | ✔ | ✔ | ✔ | | Turn-level |
| EmpathicDialogues | ✔ | ✔ | | ✔ | ✔ | ✔ | ✔ | | Turn-level |
| Holl-E | ✔ | | | ✔ | ✔ | ✔ | ✔ | | Turn-level |
| MEENA | ✔ | | | ✔ | ✔ | ✔ | ✔ | | Turn-level |
| MELD | ✔ | | | ✔ | ✔ | ✔ | ✔ | | Turn-level |
| MetalWOz | ✔ | | | ✔ | ✔ | ✔ | ✔ | | Turn-level |
| Movie-DiC | ✔ | | | ✔ | ✔ | ✔ | ✔ | | Turn-level |
| PersonaChat | ✔ | ✔ | | ✔ | ✔ | ✔ | ✔ | | Turn-level |
| SentimentLIAR | ✔ | | | ✔ | ✔ | ✔ | ✔ | | Turn-level |
| Switchboard Coherence | ✔ | | | ✔ | ✔ | ✔ | ✔ | | Turn-level |
| Topical-Chat | ✔ | ✔ | | ✔ | ✔ | ✔ | ✔ | | Turn-level |
| Wizard of Wikipedia | ✔ | ✔ | | ✔ | ✔ | ✔ | ✔ | | Turn-level |
| WOCHAT | ✔ | | | ✔ | ✔ | ✔ | ✔ | | Turn-level |

DSTC10 dataset is Task 1 and Task 2 oriented. The source language is English.

| DSTC10 | Spanish<br/>Translation | Chinese<br/>Translation | English<br/>Translation | English<br/>Back-translation | Paraphrases | Sentiment<br/>Analysis | Content<br/>Moderate | Human<br/>Annotations | Annotation<br/>Granularity |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| CONVAI2-GRADE (CG) | ✔ | ✔ | | ✔ | ✔ | ✔ | ✔ | ✔ | Turn-level |
| DAILYDIALOG-GRADE (DH) | ✔ | ✔ | | ✔ | ✔ | ✔ | ✔ | ✔ | Turn-level |
| DAILYDIALOG-GUPTA (DG) | ✔ | ✔ | | ✔ | ✔ | ✔ | ✔ | ✔ | Turn-level |
| DAILYDIALOG-ZHAO (DZ) | ✔ | ✔ | | ✔ | ✔ | ✔ | ✔ | ✔ | Turn-level |
| DSTC7 (D7) | ✔ | ✔ | | ✔ | ✔ | ✔ | ✔ | ✔ | Turn-level |
| EMPATHETIC-GRADE (EG) | ✔ | ✔ | | ✔ | ✔ | ✔ | ✔ | ✔ | Turn-level |
| FED-DIAL (FD) | ✔ | ✔ | | ✔ | ✔ | ✔ | ✔ | ✔ | Dialogue-level |
| FED-TURN (FT) | ✔ | ✔ | | ✔ | ✔ | ✔ | ✔ | ✔ | Turn-level |
| HUMOD (HU) | ✔ | ✔ | | ✔ | ✔ | ✔ | ✔ | ✔ | Turn-level |
| PERSONA-SEE (PS) | ✔ | ✔ | | ✔ | ✔ | ✔ | ✔ | ✔ | Dialogue-level |
| PERSONA-USR (PU) | ✔ | ✔ | | ✔ | ✔ | ✔ | ✔ | ✔ | Turn-level |
| PERSONA-ZHAO (PZ) | ✔ | ✔ | | ✔ | ✔ | ✔ | ✔ | ✔ | Turn-level |
| TOPICAL-USR (TU) | ✔ | ✔ | | ✔ | ✔ | ✔ | ✔ | ✔ | Turn-level |

CDIAL dataset is Task 1 oriented. The source language is Chinese.

| CDIAL | Spanish<br/>Translation | Chinese<br/>Translation | English<br/>Translation | English<br/>Back-translation | Paraphrases | Sentiment<br/>Analysis | Content<br/>Moderate | Human<br/>Annotations |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| ECM | | | ✔ | | | | | ✔ |
| KDCONV | | | ✔ | | | | | ✔ |
| LCCC | | | ✔ | | | | | ✔ |

# Data Format

All data given follows the [Data Formats](/dstc11/track4-datasets-format.md) which provides guidelines on how to store, maintain and handle dialogue corpora.

# Annex: Existing Datasets for Benchmarking

Correlation analysis on **DSTC6 human evaluation data** (Hori et al., 2017). The DSTC6 evaluation dataset contains generated responses from 20 systems for the 2000 dialogue contexts in the test set. Each generated response is annotated by 10 different Turkers using a 5-point Likert Scale. The annotation is based on whether the responses are relevant to the respective dialogue context. For each dialogue context, there are 11 gold reference responses including the original response.

Correlation analysis on **DSTC7 human evaluation data** (Galley et al., 2019). In the evaluation dataset, there are 1000 dialogue contexts and 10 responses per context. These 10 responses contain hypotheses from 9 different generative models plus the original human response. For each dialogue response, three crowd-sourced annotators provided scores based on two criteria, relevance and informativeness. The scores for each criterion are based on the 5-point Likert scale. The overall score is obtained by combining the two judgments with equal weights.

Correlation analysis on **Persona-Chatlog dataset** (See et al., 2019). The Persona-Chatlog evaluation dataset contains 3,316 conversations from 26 model configurations, which include a human agent. The annotation is performed at the conversation level whereby a crowdworker interactively chats with one model configuration for 6 conversational turns. At the end of the conversation, the crowdworker answers eight multiple-choice questions. Each question captures one aspect of conversational quality including avoiding repetition, interestingness, making sense, fluency, listening, inquisitiveness, humanness, and engagingness. All the questions use a 1-4 Likert scale, the higher the better. On average, there are 114 conversations per model configuration and each model configuration has been annotated with over 100 crowdworkers.
 
Correlation analysis on **USR dataset** (Mehri & Eskenazi, 2020). This evaluation dataset contains two parts, **USR-Persona** and **USR-Topical**. USR-Persona contains 60 test cases from the Persona-Chat (Zhang et al., 2018) domain. Each test case has a unique dialogue context. Three different generative models were trained on the PERSONA-CHAT dataset. The corresponding responses produced by these three generative models conditioning on the 60 dialogue contexts together with the original ground-truth and newly human written responses form a total of 300 context-response pairs. Each pair is annotated by three dialogue researchers along six aspects based on different Likert scales: understandability (0-1), naturalness (1-3), maintaining context (1-3), interestingness (1-3), using knowledge (0-1) and overall quality (1-5). USR-Topical contains 60 test cases from the Topical-Chat (Gopalakrishnan et al., 2019) domain. The setting is similar to USR-Persona.

Correlation analysis on **FED dataset** (Mehri & Eskenazi, 2020). The FED dataset consists of 124 conversations, out of which 40 come from Meena, 44 come from Mitsuku and another 40 are drawn from human-human conversations. Quality annotations are performed at both the dialogue level and turn level. There were 9 dialogue aspects for turn-level annotation and 11 for dialog-level annotation. In total, the FED dataset includes 3348 turn-level and 1364 dialog-level data points, for a total of 4712.

**The ChatEval dataset** (Sedoc et al., 2019) includes the Neural Conversational Model (NCM) and English as a Second Language (ESL) datasets. The NCM dataset is a collection of hand-crafted 200 single-turn prompts developed by Vinyals and Le (2015). The 200 ESL dialogue segments are from an English learning website. NCM and ESL datasets contain pairwise comparisons between system responses. NCM has 59 comparisons between 11 systems and 2 human baselines with at least 3 annotators for each prompt. The dataset has over 33K pairwise comparisons. ESL has 21 comparisons of 5 systems and a human baseline with just over 13K judgments (Lee, Lim, and Sedoc, 2020).

**The DSTC10 dataset** (Zhang et al., 2021) contains 5 datasets that were collected and manually annotated. In total, 500 dialogue segments were sampled from the conversations in the test set of TopicalChat and PersonaChat, respectively. In total, this dataset consists of 4500 context-response pairs (9 responses per context) for Topical-DTSC10 and 5000 context-response pairs (10 responses per context) for Persona-DSTC10. Each context-response pair was rated by four annotators. State of the art chatbots, including DialogGPT, GTP3, and BlenderBot, were used for the human-annotation.

# References

Zhang, C., Sadoc, J., D'Haro, L. F., Banchs, R., & Rudnicky, A. (2021). Automatic Evaluation and Moderation of Open-domain Dialogue Systems. arXiv preprint arXiv:2111.02110.

Hori, C., & Hori, T. (2017). End-to-end conversation modeling track in DSTC6. arXiv preprint arXiv:1706.07440.

Galley, M., Brockett, C., Gao, X., Gao, J., & Dolan, B. (2019). Grounded response generation task at dstc7. In AAAI Dialog System Technology Challenges Workshop.

See, A., Roller, S., Kiela, D., & Weston, J. (2019). What makes a good conversation? how controllable attributes affect human judgments. arXiv preprint arXiv:1902.08654.

Sedoc, J., Ippolito, D., Kirubarajan, A., Thirani, J., Ungar, L., & Callison-Burch, C. (2019, June). Chateval: A tool for chatbot evaluation. In Proceedings of the 2019 conference of the North American chapter of the association for computational linguistics (demonstrations) (pp. 60-65).

Vinyals, O., & Le, Q. (2015). A neural conversational model. arXiv preprint arXiv:1506.05869.

Lee, S., Lim, H., & Sedoc, J. (2020). An evaluation protocol for generative conversational systems. arXiv preprint arXiv:2010.12741.

Mehri, S., & Eskenazi, M. (2020). USR: An Unsupervised and Reference Free Evaluation Metric for Dialog Generation. arXiv preprint arXiv:2005.00456.

Mehri, S., & Eskenazi, M. (2020, July). Unsupervised Evaluation of Interactive Dialog with DialoGPT. In Proc. of the 21th Annual Meeting of the Special Interest Group on Discourse and Dialogue (pp. 225-235).

Rudnicky, A., Banchs, R., D'Haro, L. F., Sedoc, J., Chen, Z., Rodríguez-Cantelar, M., Koh, A., & others. (2020). CHANEL-Metrics: Chat/Dialogue Modeling and Evaluation report. In 2020 Seventh Frederick Jelinek Memorial Summer Workshop.

Higashinaka, R., Funakoshi, K., Kobayashi, Y., & Inaba, M. (2016, May). The dialogue breakdown detection challenge: Task description, datasets, and evaluation metrics. In Proceedings of the Tenth International Conference on Language Resources and Evaluation (LREC'16) (pp. 3146-3150).

Zhou, K., Prabhumoye, S., & Black, A. W. (2018). A dataset for document grounded conversations. arXiv preprint arXiv:1809.07358.

Danescu-Niculescu-Mizil, C., & Lee, L. (2011). Chameleons in imagined conversations: A new approach to understanding coordination of linguistic style in dialogs. arXiv preprint arXiv:1106.3077.

Li, Y., Su, H., Shen, X., Li, W., Cao, Z., & Niu, S. (2017). Dailydialog: A manually labelled multi-turn dialogue dataset. arXiv preprint arXiv:1710.03957.

Nie, Y., Williamson, M., Bansal, M., Kiela, D., & Weston, J. (2020). I like fish, especially dolphins: Addressing Contradictions in Dialogue Modeling. arXiv preprint arXiv:2012.13391.

Chen, S. Y., Hsu, C. C., Kuo, C. C., & Ku, L. W. (2018). Emotionlines: An emotion corpus of multi-party conversations. arXiv preprint arXiv:1802.08379.

Rashkin, H., Smith, E. M., Li, M., & Boureau, Y. L. (2018). Towards empathetic open-domain conversation models: A new benchmark and dataset. arXiv preprint arXiv:1811.00207.

Moghe, N., Arora, S., Banerjee, S., & Khapra, M. M. (2018). Towards exploiting background knowledge for building conversation systems. arXiv preprint arXiv:1809.08205.

Adiwardana, D., Luong, M. T., So, D. R., Hall, J., Fiedel, N., Thoppilan, R., ... & Le, Q. V. (2020). Towards a human-like open-domain chatbot. arXiv preprint arXiv:2001.09977.

Poria, S., Hazarika, D., Majumder, N., Naik, G., Cambria, E., & Mihalcea, R. (2018). Meld: A multimodal multi-party dataset for emotion recognition in conversations. arXiv preprint arXiv:1810.02508.

Lee, S., Schulz, H., Atkinson, A., Gao, J., Suleman, K., El Asri, L., ... & Li, X. (2019). Multi-domain task-completion dialog challenge. Dialog system technology challenges, 8(9).

Banchs, R. E. (2012, July). Movie-DiC: a movie dialogue corpus for research and development. In Proceedings of the 50th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers) (pp. 203-207).

Zhang, S., Dinan, E., Urbanek, J., Szlam, A., Kiela, D., & Weston, J. (2018). Personalizing dialogue agents: I have a dog, do you have pets too?. arXiv preprint arXiv:1801.07243.

Upadhayay, B., & Behzadan, V. (2020, November). Sentimental LIAR: Extended Corpus and Deep Learning Models for Fake Claim Classification. In 2020 IEEE International Conference on Intelligence and Security Informatics (ISI) (pp. 1-6). IEEE.

Cervone, A., & Riccardi, G. (2020). Is this dialogue coherent? learning from dialogue acts and entities. arXiv preprint arXiv:2006.10157.

Gopalakrishnan, K., Hedayatnia, B., Chen, Q., Gottardi, A., Kwatra, S., Venkatesh, A., ... & AI, A. A. (2019, January). Topical-Chat: Towards Knowledge-Grounded Open-Domain Conversations. In INTERSPEECH (pp. 1891-1895).

Dinan, E., Roller, S., Shuster, K., Fan, A., Auli, M., & Weston, J. (2018). Wizard of wikipedia: Knowledge-powered conversational agents. arXiv preprint arXiv:1811.01241.

D'Haro, L. F., Shawar, B. A., & Yu, Z. (2016). REWOCHAT 2016–Shared task description report. In Proceedings of the workshop on collecting and generating resources for chatbots and conversational agents-development and evaluation (RE-WOCHAT) (p. 39).

Zhou, H., Huang, M., Zhang, T., Zhu, X., & Liu, B. (2018, April). Emotional chatting machine: Emotional conversation generation with internal and external memory. In Proceedings of the AAAI Conference on Artificial Intelligence (Vol. 32, No. 1).

Zhou, H., Zheng, C., Huang, K., Huang, M., & Zhu, X. (2020). Kdconv: A chinese multi-domain dialogue dataset towards multi-turn knowledge-driven conversation. arXiv preprint arXiv:2004.04100.

Wang, Y., Ke, P., Zheng, Y., Huang, K., Jiang, Y., Zhu, X., & Huang, M. (2020, October). A large-scale chinese short-text conversation dataset. In CCF International Conference on Natural Language Processing and Chinese Computing (pp. 91-103). Springer, Cham.

Rei, R., Stewart, C., Farinha, A. C., & Lavie, A. (2020). COMET: A neural framework for MT evaluation. arXiv preprint arXiv:2009.09025.

Damodaran, P. (2021). Parrot: Paraphrase generation for NLU.

Zhou, L., Gao, J., Li, D., & Shum, H. Y. (2020). The design and implementation of xiaoice, an empathetic social chatbot. Computational Linguistics, 46(1), 53-93.

Bao, S., He, H., Wang, F., Wu, H., & Wang, H. (2019). Plato: Pre-trained dialogue generation model with discrete latent variable. arXiv preprint arXiv:1910.07931.