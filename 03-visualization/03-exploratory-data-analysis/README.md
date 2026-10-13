# Exploratory data analysis

> **Phase 3: Data Visualization and Exploratory Analysis | Lesson 03 of 4** | Beginner+ | 35 minutes

Combine summary statistics, missingness checks, and distributions in an EDA baseline.

**Keywords:** exploratory data analysis, EDA, data science workflow.

[Phase guide](../README.md) | [Runnable Python script](lesson.py) | [Course home](../../README.md)

## What you will learn

Build the concepts before memorizing syntax. Read each step, find the matching idea in `lesson.py`, run it, and change the example.

## Concepts to understand

- **EDA:** Use summaries and plots to understand data quality and patterns before modeling.
- **Descriptive statistics:** Counts, quantiles, and means summarize observations under specific assumptions.
- **Target inspection:** Grouped summaries can motivate questions but cannot prove prediction or cause.

## Before you begin

Pandas summaries, grouped aggregation, and descriptive statistics.

## Step-by-step walkthrough

1. **Load built-in data.** Scikit-Learn supplies Iris locally, avoiding a download.

2. **Check data quality.** `describe` summarizes numeric columns and `isna` counts missing values.

3. **Compare groups.** Group sepal length by label and treat differences as hypotheses, not causal results.

## Run the Python example

From the repository root, run:

```bash
python 03-visualization/03-exploratory-data-analysis/lesson.py
```

Console output shows summary statistics, zero missing values, and class-wise means.

## Practice challenge

Add a histogram, class counts, and pair plot; write one observation and limitation.

**Checkpoint:** Explain the input, operation, and what the output can and cannot tell you.

## Common mistake to avoid

EDA is not held-out evaluation. Target-informed observations do not establish generalization.

## Continue the course

[Next lesson: Interactive Plotly charts](../04-interactive-plotly/README.md)
