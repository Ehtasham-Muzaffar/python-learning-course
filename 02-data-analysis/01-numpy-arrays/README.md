# NumPy arrays

> **Phase 2: Data Manipulation and Analysis | Lesson 01 of 4** | Beginner+ | 30 minutes

Create and reshape NumPy arrays, then compute vectorized descriptive statistics.

**Keywords:** NumPy tutorial, numerical Python, arrays.

[Phase guide](../README.md) | [Runnable Python script](lesson.py) | [Course home](../../README.md)

## What you will learn

This lesson builds the concepts before asking you to memorize syntax. Read each step, find the matching idea in `lesson.py`, run it, and change the example.

## Concepts to understand

- **ndarray:** NumPy stores homogeneous multidimensional numerical data.
- **Shape and axis:** Shape describes dimensions; `axis=0` reduces rows to each column.
- **Broadcasting:** Compatible shapes apply row-wise calculations without Python loops.

## Before you begin

Python numeric types, lists, and basic arithmetic.

## Step-by-step walkthrough

1. **Build a 2D array.** Represent two observations and three score columns.

2. **Inspect dimensions.** Check `.shape` before calculation.

3. **Reduce and broadcast.** Calculate column means and divide each row by its maximum using `keepdims=True`.

## Run the Python example

From the repository root, run:

```bash
python 02-data-analysis/01-numpy-arrays/lesson.py
```

Shape is `(2, 3)`, column means `[82., 89.5, 90.5]`, and each normalized row has maximum 1.

## Practice challenge

Add a student and calculate means across both subjects and students.

**Checkpoint:** Explain the input, operation, and what the output can and cannot tell you.

## Common mistake to avoid

Axis meaning depends on the dimension being reduced; check output shapes on a small example.

## Continue the course

[Next lesson: Pandas DataFrames](../02-pandas-dataframes/README.md)
