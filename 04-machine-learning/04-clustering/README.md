# Clustering with K-Means

> **Phase 4: Applied Machine Learning | Lesson 04 of 6** | Intermediate | 35 minutes

Scale features before K-Means and compare discovered cluster labels with known groups.

**Keywords:** unsupervised learning, K-Means, clustering.

[Phase guide](../README.md) | [Runnable Python script](lesson.py) | [Course home](../../README.md)

## What you will learn

Build the concepts before memorizing syntax. Read each step, find the matching idea in `lesson.py`, run it, and change the example.

## Concepts to understand

- **Unsupervised learning:** Group examples without fitting known target labels.
- **Feature scaling:** Distance methods may be dominated by features with larger numeric ranges.
- **K-Means:** Alternate cluster assignments and centroid updates; IDs are arbitrary.

## Before you begin

NumPy arrays, distance intuition, and feature scaling.

## Step-by-step walkthrough

1. **Load measurements.** Fit to feature measurements only, without target labels.

2. **Scale features.** Standardize columns to comparable scales before distance calculations.

3. **Fit and inspect.** Choose cluster count and seed, then count assigned records; treat the groups as exploratory.

## Run the Python example

From the repository root, run:

```bash
python 04-machine-learning/04-clustering/lesson.py
```

The script reports three cluster sizes and distinguishes them from true classes.

## Practice challenge

Try other cluster counts and seeds; compare inertia or silhouette score and visualize.

**Checkpoint:** Explain the input, operation, and what the output can and cannot tell you.

## Common mistake to avoid

Cluster IDs have no semantic meaning. Scaling and chosen cluster count are assumptions, not facts.

## Continue the course

[Next lesson: Model evaluation and cross-validation](../05-model-evaluation-and-cross-validation/README.md)
