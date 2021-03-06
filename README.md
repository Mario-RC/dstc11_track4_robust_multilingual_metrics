# DSTC11: Dialogue System Technology Challenge 11<br/><br/>Track 4: Robust and Multilingual Automatic Evaluation Metrics for Open-Domain Dialogue Systems

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Track Overview

This track consists of two tasks which are explained in more detail below:

Participants will develop effective automatic open-ended and multilingual dialogue evaluation metrics that perform similarly when evaluated over a new language.
Participants will develop effective automatic open-ended dialogue evaluation metrics that perform robustly when evaluated over back-translated/paraphrased sentences in English.
For both tasks, proposed metrics are expected to show the following two important properties as indicated in (Deriu et al., 2019):

Correlated to human judgments - the metrics should produce evaluation scores that well correlate to human judgments (scores) across multiple languages or alternative responses (i.e., back-translated or paraphrased).
Explainable - the metrics should provide constructive and explicit feedback to the generative models in terms of the quality of their generated responses. For instance, if a generative model is contradicting itself, the evaluation metrics should signal such behavior to the generative models.
Participants can propose their own metric or optionally improve two baseline evaluation metrics: MDD-Eval (Zhang et al, 2021) or deep AM-FM (Zhang et al, 2020). A leaderboard in the ChatEval platform will be provided allowing participants to check their progress.

For each evaluation task, Spearman correlation will be computed to compare the proposed evaluation metrics against human judgments. A final average score will be calculated to rank the submitted evaluation metrics.

For more details:

* [Provided datasets](/dstc11/track4-provided-datasets.md)
* [Task 1: Metrics for multilingual data](/dstc11/track4-task1-metrics-multilingual-data.md)
* [Task 2: Robust metrics](/dstc11/track4-task2-robust-metrics.md)
* [FAQ](/dstc11/track4-faq.md)

## Schedule

* **Training/Validation data release**: From November to December in 2022
* **Test data release**: Middle of March in 2023
* **Entry submission deadline**: Middle of March in 2023
* **Submission of final results**: End of March in 2023
* **Final result announcement**: Early of April in 2023
* **Paper submission**: From March to May in 2023
* **Workshop**: July, August or September in 2023

## Baselines and Data Description

For more information check the [Track Proposal](https://drive.google.com/file/d/1wHZdlz8JecDWiiJiwhP3VsKnbApdL6_e/view).

## Registration Details

For registration go to the [Registration Details section](https://chateval.org/dstc11/annex-registration-details) at the [ChatEval website](https://chateval.org/dstc11). Any updates and information about the tracks will be posted on the [DSTC11 official website](https://dstc11.dstc.community/), or check the [DSTC11 official website](https://dstc11.dstc.community/).

Any updates and information about the tracks will be posted on the DSTC11 official website, or check the [DSTC Mailing List](https://groups.google.com/a/dstc.community/g/list).

## Organizers

* Mario Rodr??guez-Cantelar (Universidad Polit??cnica de Madrid, Spain)
* Chen Zhang (National University of Singapore, Singapore)
* Chengguang Tang (Tencent AI Lab, China)
* Ke Shi (Tencent AI Lab, China)
* Jo??o Sedoc (New York University, USA)
* Luis F. D'Haro (Universidad Polit??cnica de Madrid, Spain)
* Alexander Rudnicky (Carnegie Mellon University, USA)

## Contact

If you have further questions regarding the data, please let us know by the following email address at [dstc11-robust-multilingual-automatic-evaluation@googlegroups.com](dstc11-robust-multilingual-automatic-evaluation@googlegroups.com).

## References

Deriu, J., Rodrigo, A., Otegi, A., Echegoyen, G., Rosset, S., Agirre, E., & Cieliebak, M. (2020). Survey on evaluation methods for dialogue systems. Artificial Intelligence Review, 1-56.

Zhang, C., D'Haro, L. F., Friedrichs, T., & Li, H. (2021). MDD-Eval: Self-Training on Augmented Data for Multi-Domain Dialogue Evaluation. arXiv preprint arXiv:2112.07194.

Zhang, C., D'Haro, L. F., Banchs, R. E., Friedrichs, T., & Li, H. (2020). Deep AM-FM: Toolkit for Automatic Dialogue Evaluation. In Conversational Dialogue Systems for the Next Decade (pp. 53-69). Springer, Singapore.