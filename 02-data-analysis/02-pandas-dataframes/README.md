# Pandas DataFrames

> **Phase 2: Data Manipulation and Analysis | Lesson 02 of 4** | Beginner+ | 35 minutes

Inspect, filter, and aggregate tabular records with Pandas.

**Keywords:** Pandas tutorial, DataFrame, data analysis.

[Phase guide](../README.md) | [Runnable Python script](lesson.py) | [Course home](../../README.md)

## What you will learn

This lesson builds the concepts before asking you to memorize syntax. Read each step, find the matching idea in `lesson.py`, run it, and change the example.

## Concepts to understand

- **DataFrame:** A labeled table with named columns and an index.
- **Boolean filter:** A condition creates a mask for selecting rows.
- **Group-by:** Partition records by category and aggregate per group.

## Before you begin

Python dictionaries, lists, and basic tabular thinking.

## Step-by-step walkthrough

1. **Build a table.** Each row is a team observation; column lengths must agree.

2. **Filter.** Use a score comparison as a Boolean mask.

3. **Aggregate.** Group hours by team, calculate the mean, and keep the team key as a column.

## Run the Python example

From the repository root, run:

```bash
python 02-data-analysis/02-pandas-dataframes/lesson.py
```

Qualifying rows are selected and the mean hours for both teams is 4.

## Practice challenge

Add dates, filter a range, and report score mean and observation count per team.

**Checkpoint:** Explain the input, operation, and what the output can and cannot tell you.

## Common mistake to avoid

Inspect data types and missingness before trusting aggregate results.

## Continue the course

[Next lesson: Data cleaning](../03-data-cleaning/README.md)
