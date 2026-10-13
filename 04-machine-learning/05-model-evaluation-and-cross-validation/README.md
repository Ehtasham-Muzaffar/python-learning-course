# Model evaluation and cross-validation

> **Phase 4: Applied Machine Learning | Lesson 05 of 6** | Intermediate | 40 minutes

Estimate classifier performance with stratified cross-validation and inspect multiple metrics.

**Keywords:** model evaluation, cross-validation, ML metrics.

[Phase guide](../README.md) | [Runnable Python script](lesson.py) | [Course home](../../README.md)

## What you will learn

Build the concepts before memorizing syntax. Read each step, find the matching idea in `lesson.py`, run it, and change the example.

## Concepts to understand

- **Cross-validation:** Fit on several folds and score held-out folds to estimate average and variability.
- **Stratification:** Classification folds preserve approximate class proportions.
- **Metric choice:** Metrics represent different errors and should match the application.

## Before you begin

Classification, preprocessing pipelines, precision, recall, and F1.

## Step-by-step walkthrough

1. **Choose model and metrics.** The pipeline keeps scaling inside each fold and computes three complementary metrics.

2. **Define folds.** Shuffling and a seed make the demonstration repeatable.

3. **Inspect fold scores.** `cross_validate` returns per-fold scores; average them as a compact summary.

## Run the Python example

From the repository root, run:

```bash
python 04-machine-learning/05-model-evaluation-and-cross-validation/lesson.py
```

Output shows mean accuracy, precision, and recall across five folds.

## Practice challenge

Print each fold and standard deviation; choose a primary metric for a stated use case.

**Checkpoint:** Explain the input, operation, and what the output can and cannot tell you.

## Common mistake to avoid

A mean alone can conceal variance. Leakage, imbalance, and non-independent rows may invalidate the estimate.

## Continue the course

[Next lesson: Hyperparameter tuning](../06-hyperparameter-tuning/README.md)
