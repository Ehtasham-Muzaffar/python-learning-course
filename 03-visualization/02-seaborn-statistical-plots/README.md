# Seaborn statistical plots

> **Phase 3: Data Visualization and Exploratory Analysis | Lesson 02 of 4** | Beginner+ | 35 minutes

Compare distributions across categories with a labeled Seaborn box plot.

**Keywords:** Seaborn tutorial, statistical visualization, Python EDA.

[Phase guide](../README.md) | [Runnable Python script](lesson.py) | [Course home](../../README.md)

## What you will learn

Build the concepts before memorizing syntax. Read each step, find the matching idea in `lesson.py`, run it, and change the example.

## Concepts to understand

- **Distribution:** A distribution describes range, center, and variation.
- **Box plot:** Quartiles and median summarize groups; whisker/outlier conventions matter.
- **Long-form data:** One observation per row maps categories and measurements cleanly.

## Before you begin

Pandas DataFrames and basic Matplotlib.

## Step-by-step walkthrough

1. **Inspect tidy sample.** The script builds an offline category and bill-value table.

2. **Map fields.** Put category on x and numeric measurements on y to compare groups.

3. **Label and compare.** Look at medians, spread, and group sizes before interpreting differences.

## Run the Python example

From the repository root, run:

```bash
python 03-visualization/02-seaborn-statistical-plots/lesson.py
```

A box plot compares example bills across weekdays without downloading data.

## Practice challenge

Show individual points and sample counts so readers can see group size.

**Checkpoint:** Explain the input, operation, and what the output can and cannot tell you.

## Common mistake to avoid

Visible differences do not prove significance or causality; explain what the plot shows.

## Continue the course

[Next lesson: Exploratory data analysis](../03-exploratory-data-analysis/README.md)
