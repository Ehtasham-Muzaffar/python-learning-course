# Vectorization and feature preparation

> **Phase 2: Data Manipulation and Analysis | Lesson 04 of 4** | Beginner+ | 30 minutes

Use vectorized column operations to create a feature without a Python row loop.

**Keywords:** vectorization, feature engineering, Pandas performance.

[Phase guide](../README.md) | [Runnable Python script](lesson.py) | [Course home](../../README.md)

## What you will learn

Build the concepts before memorizing syntax. Read each step, find the matching idea in `lesson.py`, run it, and change the example.

## Concepts to understand

- **Vectorization:** Array and Series operations process many values in optimized library code.
- **Feature engineering:** Transform existing columns into more useful model inputs.
- **Boolean feature:** A threshold creates an explicit true/false column.

## Before you begin

Pandas arithmetic, Boolean comparisons, and DataFrame columns.

## Step-by-step walkthrough

1. **Inspect inputs.** Each row has numeric quantity and unit price.

2. **Build a vectorized feature.** Multiply aligned Series to create the per-row total without a row loop.

3. **Encode a decision.** Compare totals against a threshold to create an order-size flag.

## Run the Python example

From the repository root, run:

```bash
python 02-data-analysis/04-vectorization-and-feature-prep/lesson.py
```

The table gains numeric totals and a Boolean large-order column.

## Practice challenge

Add a discount column and compute net totals; compare with a small explicit loop.

**Checkpoint:** Explain the input, operation, and what the output can and cannot tell you.

## Common mistake to avoid

Vectorized operations align on index labels. Check indexes, nulls, and readability.

## Continue the course

[Next phase: Phase 3: Data Visualization and Exploratory Analysis](../../03-visualization/README.md)
