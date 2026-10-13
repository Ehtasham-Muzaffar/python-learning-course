# Regression

> **Phase 4: Applied Machine Learning | Lesson 02 of 6** | Intermediate | 35 minutes

Fit a baseline regression model and report held-out mean absolute error.

**Keywords:** machine learning regression, LinearRegression, Scikit-Learn.

[Phase guide](../README.md) | [Runnable Python script](lesson.py) | [Course home](../../README.md)

## What you will learn

Build the concepts before memorizing syntax. Read each step, find the matching idea in `lesson.py`, run it, and change the example.

## Concepts to understand

- **Regression:** Supervised prediction of a numeric target.
- **Linear model:** LinearRegression estimates coefficients combining features into a value.
- **MAE:** Mean absolute error averages absolute residuals in target units.

## Before you begin

Train/test splitting, numeric arrays, and Scikit-Learn basics.

## Step-by-step walkthrough

1. **Load data.** The built-in diabetes dataset contains numeric features and continuous target.

2. **Reserve test observations.** Fit only on training records.

3. **Measure predictions.** Calculate held-out MAE and retain interpretable target units.

## Run the Python example

From the repository root, run:

```bash
python 04-machine-learning/02-regression/lesson.py
```

The console reports held-out mean absolute error; results can vary by package version.

## Practice challenge

Compare against predicting the training-set mean as a baseline.

**Checkpoint:** Explain the input, operation, and what the output can and cannot tell you.

## Common mistake to avoid

A single score needs a baseline, context, and residual inspection; association is not causation.

## Continue the course

[Next lesson: Classification](../03-classification/README.md)
