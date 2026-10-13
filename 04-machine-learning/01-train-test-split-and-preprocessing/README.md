# Train-test split and preprocessing

> **Phase 4: Applied Machine Learning | Lesson 01 of 6** | Intermediate | 40 minutes

Split before fitting and keep scaling inside a Scikit-Learn pipeline to avoid leakage.

**Keywords:** Scikit-Learn preprocessing, train-test split, ML pipeline.

[Phase guide](../README.md) | [Runnable Python script](lesson.py) | [Course home](../../README.md)

## What you will learn

Build the concepts before memorizing syntax. Read each step, find the matching idea in `lesson.py`, run it, and change the example.

## Concepts to understand

- **Holdout split:** Reserve examples untouched during training for an honest generalization estimate.
- **Data leakage:** Information unavailable at prediction time must not influence training or preprocessing.
- **Pipeline:** Transforms fit on training data and stay consistent at prediction time.

## Before you begin

Feature tables, target labels, and data cleaning.

## Step-by-step walkthrough

1. **Separate features and target.** Iris measurements are inputs and species is the target.

2. **Split before fitting.** A stratified split preserves class proportions and a seed makes the example repeatable.

3. **Fit pipeline.** Scaler learns from training data, then logistic regression fits transformed features.

## Run the Python example

From the repository root, run:

```bash
python 04-machine-learning/01-train-test-split-and-preprocessing/lesson.py
```

The script reports held-out accuracy after fitting the pipeline.

## Practice challenge

Compare to scaling the complete dataset before the split and explain the leakage.

**Checkpoint:** Explain the input, operation, and what the output can and cannot tell you.

## Common mistake to avoid

Do not repeatedly tune against the test set; use training-only cross-validation and reserve a final test.

## Continue the course

[Next lesson: Regression](../02-regression/README.md)
