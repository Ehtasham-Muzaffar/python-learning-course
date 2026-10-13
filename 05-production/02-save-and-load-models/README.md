# Save and load models with Joblib

> **Phase 5: Deep Learning and Production Basics | Lesson 02 of 5** | Intermediate | 35 minutes

Persist and reload a fitted Scikit-Learn pipeline, then verify its predictions.

**Keywords:** save machine learning model, Joblib, model serialization.

[Phase guide](../README.md) | [Runnable Python script](lesson.py) | [Course home](../../README.md)

## What you will learn

Build the concepts before memorizing syntax. Read each step, find the matching idea in `lesson.py`, run it, and change the example.

## Concepts to understand

- **Serialization:** Convert an in-memory object into a file and restore it later.
- **Provenance:** A real artifact needs compatible dependencies, feature schema, and training lineage.
- **Trust boundary:** Unpickling untrusted Joblib files can execute code.

## Before you begin

A fitted Scikit-Learn estimator and basic file/path concepts.

## Step-by-step walkthrough

1. **Train an estimator.** Fit logistic regression on built-in data.

2. **Write temporary artifact.** Joblib serializes the fitted object outside the repository.

3. **Reload and verify.** Load it and compare predictions on identical example inputs.

## Run the Python example

From the repository root, run:

```bash
python 05-production/02-save-and-load-models/lesson.py
```

Predictions before and after loading match.

## Practice challenge

Save a complete preprocessing pipeline and record the library version alongside the artifact.

**Checkpoint:** Explain the input, operation, and what the output can and cannot tell you.

## Common mistake to avoid

Never load an untrusted Joblib/pickle artifact; serialization alone does not guarantee compatibility.

## Continue the course

[Next lesson: ONNX model export](../03-onnx-model-export/README.md)
