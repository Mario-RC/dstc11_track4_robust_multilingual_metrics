# Baseline Model

The purpose of this project is to identify a baseline classifier for DSTC-11. The default choice is Deep AM-FM (Zhang et al, 2020) (used for DSTC-10 and previously).

This project will investigate more recent approaches, based on fine-tuned large language models. Zhang et al note that their approach may be limited due to domain specificity. On the other hand LLMs are trained from large corpora that in priciple are less domain-dependent. This is an empirical question.

# Model Description

All information related to the baseline model, such as code and data, can be found in this [GitHub](https://github.com/karthik19967829/DSTC11-Benchmark) repository.

# Automatic Evaluation Results

The leaderboard shows the corresponding Spearman Correlation Coefficients for each development dataset obtained by the baseline model. The name of each column corresponds to an [abbreviation](https://github.com/Mario-RC/dstc11_track4_robust_multilingual_metrics/blob/main/dstc11/track4-provided-datasets.md#provided-datasets) of the development datasets respectively.

## Task 1: Metrics for Multilingual Data (development)

| System | CG | DH | DG | DZ | D7 | EG | FD | FT | HM | PS | PU | PZ | TU | AVG |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| AM-FM ES | 0.3094 | 0.1053 | 0.2146 | 0.1170 | 0.2317 | 0.2001 | 0.1172 | -0.0120 | 0.1019 | 0.0236 | 0.0634 | 0.4118 | 0.1086 | 0.1551 |
| AM-FM ZH | 0.2989 | 0.0873 | 0.2382 | 0.1391 | 0.2206 | 0.2115 | 0.0819 | -0.0254 | 0.0990 | 0.0198 | 0.0849 | 0.3821 | 0.0849 | 0.1518 |


## Task 2: Robust Metrics (development)

| System | CG | DH | DG | DZ | D7 | EG | FD | FT | HM | PS | PU | PZ | TU | AVG |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| AM-FM | 0.2842 | 0.0512 | 0.2879 | 0.1356 | 0.0374 | 0.2452 | 0.1243 | -0.0039 | 0.1080 | 0.0192 | 0.0730 | 0.4241 | 0.0872 | 0.1447 |

# References

Zhang, C., D'Haro, L. F., Banchs, R. E., Friedrichs, T., & Li, H. (2020). Deep AM-FM: Toolkit for Automatic Dialogue Evaluation. In Conversational Dialogue Systems for the Next Decade (pp. 53-69). Springer, Singapore.