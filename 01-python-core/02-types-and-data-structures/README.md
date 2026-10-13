# Types and data structures

> **Phase 1: Modern Python Core | Lesson 02 of 5** | Beginner | 25 minutes

Represent a small dataset with Python strings, numbers, lists, dictionaries, and sets.

**Keywords:** Python data types, collections, beginner Python.

[Phase guide](../README.md) | [Runnable Python script](lesson.py) | [Course home](../../README.md)

## What you will learn

This lesson builds the concepts before asking you to memorize syntax. Read each step, find the matching idea in `lesson.py`, run it, and change the example.

## Concepts to understand

- **Scalar types:** `str`, `int`, `float`, and `bool` represent text, integers, decimals, and truth.
- **Collections:** Lists preserve order, dictionaries map keys to values, and sets keep unique values.
- **Mutability:** Lists and dictionaries change in place; tuples and strings do not.

## Before you begin

Lesson 1; know how to run a script.

## Step-by-step walkthrough

1. **Inspect a dictionary.** The student record groups a name, scores, and an active flag.

2. **Select numeric types.** Scores are integers, while a mean may be a float.

3. **Summarize.** `sum` and `len` calculate an average; `set` demonstrates uniqueness, not sorting.

## Run the Python example

From the repository root, run:

```bash
python 01-python-core/02-types-and-data-structures/lesson.py
```

The output includes the average and unique scores. Set display order is not guaranteed.

## Practice challenge

Add a subject-score mapping and compute one subject average.

**Checkpoint:** Explain the input, operation, and what the output can and cannot tell you.

## Common mistake to avoid

Sets discard duplicates and have no positional index; avoid them when order matters.

## Continue the course

[Next lesson: Control flow and iteration](../03-control-flow-and-iteration/README.md)
