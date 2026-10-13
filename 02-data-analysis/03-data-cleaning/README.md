# Data cleaning

> **Phase 2: Data Manipulation and Analysis | Lesson 03 of 4** | Beginner+ | 35 minutes

Handle missing values, duplicate rows, and explicit Pandas dtypes in a small dataset.

**Keywords:** data cleaning with Pandas, missing data, preprocessing.

[Phase guide](../README.md) | [Runnable Python script](lesson.py) | [Course home](../../README.md)

## What you will learn

This lesson builds the concepts before asking you to memorize syntax. Read each step, find the matching idea in `lesson.py`, run it, and change the example.

## Concepts to understand

- **Missingness:** Unknown is not automatically zero; meaning depends on data collection.
- **Duplicates:** Repeated rows may be valid events or ingestion errors; use context.
- **Dtype:** Explicit types make calculations predictable.

## Before you begin

Pandas DataFrames, column selection, and summaries.

## Step-by-step walkthrough

1. **Inspect the sample.** Review the missing age and repeated observation.

2. **Remove a true duplicate.** Use `drop_duplicates` and copy the working table.

3. **Impute and validate.** Fill this example with the median, cast the type, then inspect results.

## Run the Python example

From the repository root, run:

```bash
python 02-data-analysis/03-data-cleaning/lesson.py
```

The duplicate is removed; age is median-filled with integer dtype.

## Practice challenge

Compare median imputation with dropping the missing row and note the effects.

**Checkpoint:** Explain the input, operation, and what the output can and cannot tell you.

## Common mistake to avoid

Imputation changes distributions; document why values are missing and the policy used.

## Continue the course

[Next lesson: Vectorization and feature preparation](../04-vectorization-and-feature-prep/README.md)
