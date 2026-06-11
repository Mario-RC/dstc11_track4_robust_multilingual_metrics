# Local Data

This directory is intentionally ignored by Git, except for this README.

Download the public dataset release from Hugging Face and place it here when working locally:

```text
data/DSTC_11_Track_4/
```

The public dataset reference is:

```text
https://huggingface.co/datasets/mario-rc/dstc11.t4
```

Do not upload this directory to GitHub.

The public Hugging Face release intentionally excludes held-out test data. If test data is needed for research or evaluation, request access from the DSTC11 Track 4 organizers.

Derived MTQE and paraphrase scores should be regenerated into `outputs/` or another ignored local directory. See:

```text
docs/data-and-regeneration.md
```
