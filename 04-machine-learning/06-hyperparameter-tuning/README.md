# Hyperparameter tuning

> **Phase 4: Applied Machine Learning | Lesson 06 of 6** | Intermediate | 45 minutes

Tune a pipeline with cross-validation and evaluate the selected estimator on held-out data.

**Keywords:** hyperparameter tuning, GridSearchCV, model selection.

[Phase guide](../README.md) | [Runnable Python script](lesson.py) | [Course home](../../README.md)

## What you will learn

Build the concepts before memorizing syntax. Read each step, find the matching idea in `lesson.py`, run it, and change the example.

## Concepts to understand

- **Hyperparameter:** A setting selected before model fitting, unlike learned coefficients.
- **Grid search:** Evaluate declared parameter combinations using cross-validation.
- **Nested evaluation:** Select using training data and keep final test data untouched.

## Before you begin

Pipelines, holdout testing, cross-validation, and model evaluation.

## Step-by-step walkthrough

1. **Hold out final test.** Split once so the final score cannot influence model selection.

2. **Declare pipeline and search.** Tune SVC parameters with pipeline-qualified names; refit preprocessing per fold.

3. **Evaluate once.** Inspect best CV settings, then score selected estimator on test data.

## Run the Python example

From the repository root, run:

```bash
python 04-machine-learning/06-hyperparameter-tuning/lesson.py
```

The script reports best settings and final held-out accuracy.

## Practice challenge

Compare another classifier and record search cost without choosing parameters on test score.

**Checkpoint:** Explain the input, operation, and what the output can and cannot tell you.

## Common mistake to avoid

Repeatedly trying settings against the test partition overfits the evaluation.

## Continue the course

[Next phase: Phase 5: Deep Learning and Production Basics](../../05-production/README.md)
