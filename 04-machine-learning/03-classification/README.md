# Classification

> **Phase 4: Applied Machine Learning | Lesson 03 of 6** | Intermediate | 40 minutes

Train a classifier and inspect class-wise precision, recall, and confusion counts.

**Keywords:** classification, logistic regression, Scikit-Learn.

[Phase guide](../README.md) | [Runnable Python script](lesson.py) | [Course home](../../README.md)

## What you will learn

Build the concepts before memorizing syntax. Read each step, find the matching idea in `lesson.py`, run it, and change the example.

## Concepts to understand

- **Classification:** Predict a category rather than an unrestricted continuous measurement.
- **Logistic regression:** A linear classifier estimates class probabilities.
- **Precision and recall:** Precision measures correctness of positive predictions; recall measures positives found.

## Before you begin

Train/test splits, target labels, and feature scaling.

## Step-by-step walkthrough

1. **Choose target.** The built-in dataset has a binary target and readable labels.

2. **Split stratified.** Keep approximate class balance in train and test subsets.

3. **Scale, fit, inspect.** Use a pipeline then report per-class precision, recall, and F1.

## Run the Python example

From the repository root, run:

```bash
python 04-machine-learning/03-classification/lesson.py
```

The classification report lists metrics and support for each held-out class.

## Practice challenge

Use `predict_proba`, vary the threshold, and compare false positive and negative counts.

**Checkpoint:** Explain the input, operation, and what the output can and cannot tell you.

## Common mistake to avoid

Accuracy can hide minority-class failures; select metrics for error costs. This is not a clinical tool.

## Continue the course

[Next lesson: Clustering with K-Means](../04-clustering/README.md)
