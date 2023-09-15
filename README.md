# DSTC11: Dialogue System Technology Challenge 11<br/><br/>Track 4: Robust and Multilingual Automatic Evaluation Metrics for Open-Domain Dialogue Systems

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# Track Overview

This track consists of two tasks which are explained in more detail below:

Participants will develop effective automatic open-ended and multilingual dialogue evaluation metrics that perform similarly when evaluated over a new language.
Participants will develop effective automatic open-ended dialogue evaluation metrics that perform robustly when evaluated over back-translated/paraphrased sentences in English.
For both tasks, proposed metrics are expected to show the following two important properties as indicated in (Deriu et al., 2019):

Correlated to human judgments - the metrics should produce evaluation scores that well correlate to human judgments (scores) across multiple languages or alternative responses (i.e., back-translated or paraphrased).

Explainable - the metrics should provide constructive and explicit feedback to the generative models in terms of the quality of their generated responses. For instance, if a generative model is contradicting itself, the evaluation metrics should signal such behavior to the generative models.

Participants can propose their own metric or optionally improve two baseline evaluation metrics: MDD-Eval (Zhang et al, 2021) or Deep AM-FM (Zhang et al, 2020). A leaderboard in the ChatEval platform will be provided allowing participants to check their progress.

For each evaluation task, Spearman correlation will be computed to compare the proposed evaluation metrics against human judgments. A final average score will be calculated to rank the submitted evaluation metrics.

For more details:

* [Provided datasets](./dstc11/track4-provided-datasets.md)
* [Datasets format](./dstc11/track4-datasets-format.md)
* [Task 1: Multilingual Automatic Evaluation Metrics](./dstc11/track4-task1-multilingual-metrics.md)
* [Task 2: Robust Automatic Evaluation Metrics](./dstc11/track4-task2-robust-metrics.md)
* [Baseline model](./dstc11/track4-baseline-model.md)
* [FAQ](./dstc11/track4-faq.md)

For more information check the [Track Proposal](https://drive.google.com/file/d/1wHZdlz8JecDWiiJiwhP3VsKnbApdL6_e/view).

# Schedule 

* **Training/Validation data release**: Dec 14, 2022
* **Test data release**: Mar 29, 2023
* **Entry submission deadline**: Apr 3, 2023 (23:59 Anywhere on Earth (AoE), UTC-12)
* **Final result announcement**: Apr 14, 2023
* **Paper submission**: June 2nd, 2023
* **Workshop**: September 11 or 12, at SIGDIAL x INLG 2023 in Prague, Czech Republic

# Registration Details

For registration go to the [Registration Details section](https://chateval.org/dstc11/annex-registration-details) at the [ChatEval website](https://chateval.org/dstc11).

There must be only one team per laboratory or research group. The members of the same team must be under a single registration, that is, the team leader must register his entire team by giving their e-mail addresses in addition to his own.

Any updates and information about the tracks will be posted on the [DSTC11 official website](https://dstc11.dstc.community/), or check the [DSTC11 official website](https://dstc11.dstc.community/).

# Submission Details

Before submitting your results, do not forget to [Sign Up](https://my.chateval.org/accounts/signup/) on the ChatEval website. Only the team leader must register on ChatEval, with the same name and email address entered in the Microsoft Form. Once you have signed up, you can [Log In](https://my.chateval.org/accounts/login/) and [Submit](https://my.chateval.org/dstc11submit/) your  evaluations.

There are four different evaluations to test the models, namely:

* Task 1 - Turn-Level
* Task 1 - Dialogue-Level
* Task 2 - Turn-Level
* Task 2 - Dialogue-Level

Each task has annotations at turn-level and dialogue-level, so the models will be evaluated separately at turn-level and dialogue-level independently for each task, they will not be taken into account together at any level. That is, for Task 1 the models at turn-level and at dialogue-level will be evaluated separately, likewise, for Task 2 the models at turn-level and at dialogue-level will be evaluated separately.

If you want, you can participate in as many evaluations as you want. Whether you only want to participate in one, several or all of the evaluations, the scores obtained will be independent, unrelated to the other scores, and will not be combined for the final score. There will be a table with the scores obtained for each of the 4 different evaluations.

You can submit as many score files as you want for each evaluation, but only the last 5 files submitted for each type of evaluation in ChatEval will be valid and will count in the ranking to participate in the competition. Moreover, only the evaluations submitted by the team leader registered in the Microsoft form will be considered and count towards the competition.

In order to submit test data evaluations, they must be named appropriately. Below is the correct way to name the test files that should be sent correctly annotated:

* \<team_name>_task1_turn_v\<x>.csv
* \<team_name>_task1_dial_v\<x>.csv
* \<team_name>_task2_turn_v\<x>.csv
* \<team_name>_task2_dial_v\<x>.csv

Please specify clearly in the submission name which evaluation it is intended for, the team name in <team_name> and the submission version <x> to identify the submission.

# Organizers

* Mario Rodríguez-Cantelar (Universidad Politécnica de Madrid, Spain)
* Chen Zhang (National University of Singapore, Singapore)
* Chengguang Tang (Tencent AI Lab, China)
* Ke Shi (Tencent AI Lab, China)
* Sarik Ghazarian (University of Southern California, USA)
* João Sedoc (New York University, USA)
* Luis F. D'Haro (Universidad Politécnica de Madrid, Spain)
* Alexander Rudnicky (Carnegie Mellon University, USA)

# Contact

If you have further questions regarding the data, please let us know by the following email address at [dstc11-robust-multilingual-automatic-evaluation@googlegroups.com](dstc11-robust-multilingual-automatic-evaluation@googlegroups.com).

# Citation

Please cite the paper, code or data from DSTC 11 Track 4:
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

# Acknowledgement

This research project is supported by the Comunidad de Madrid through the call Research Grants for Young Investigators from Universidad Politécnica de Madrid (GENIUS:APOYO-JOVENES-21-TAXTYC-32-K61X37).

This work is supported by project BEWORD (PID2021-126061OB-C43) funded by MCIN/AEI/10.13039/501100011033 and, as appropriate, by “ERDF A way of making Europe”, by the “European Union”, and by Programa Propio - Proyectos Semilla: Universidad Politécnica de Madrid (VSEMILLA22LFHE).

We gratefully acknowledge valuable efforts from Tencent AI Lab who supports Chinese translation and annotation of datasets by funding and infrastructure.

Thanks to THU-CoAI (Conversational AI groups from Tsinghua University) for providing their Chinese datasets as part of the challenge data.

Thanks to Unbabel for providing the COMET MTQE scores annotations as part of the challenge data. This contribution was supported by national funds through *Fundação para a Ciência e a Tecnologia* (FCT) with references PRT/BD/152198/2021 and UIDB/50021/2020, and by the P2020 program MAIA led by Unbabel (LISBOA-01-0247-FEDER-045909).

We also want to give thanks to MS Azure services (especially to Irving Kwong) for their sponsorship to continue processing new datasets that could be interesting for the dialogue community.

This research project is supported by the NYU ChatEval Team led by João Sedoc.

This research project is supported in part by a grant from Amazon to Alexander Rudnicky, Carnegie Mellon University.

Thanks to Karthik Ganesan, Sarik Ghazarian, James Hagerty, Zhang Chen and Alex Rudnicky for developing the baseline model as part of the challenge tasks.

This work is supported by the European Commission through Project ASTOUND (101071191 — HORIZON-EIC-2021-PATHFINDERCHALLENGES-01).

![alt text](./img/Logo_EC.png)

# References

Deriu, J., Rodrigo, A., Otegi, A., Echegoyen, G., Rosset, S., Agirre, E., & Cieliebak, M. (2020). Survey on evaluation methods for dialogue systems. Artificial Intelligence Review, 1-56.

Zhang, C., D'Haro, L. F., Friedrichs, T., & Li, H. (2021). MDD-Eval: Self-Training on Augmented Data for Multi-Domain Dialogue Evaluation. arXiv preprint arXiv:2112.07194.

Zhang, C., D'Haro, L. F., Banchs, R. E., Friedrichs, T., & Li, H. (2020). Deep AM-FM: Toolkit for Automatic Dialogue Evaluation. In Conversational Dialogue Systems for the Next Decade (pp. 53-69). Springer, Singapore.
