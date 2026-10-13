# Control flow and iteration

> **Phase 1: Modern Python Core | Lesson 03 of 5** | Beginner | 25 minutes

Filter records with conditions and safely handle invalid values while iterating.

**Keywords:** Python control flow, loops, comprehensions.

[Phase guide](../README.md) | [Runnable Python script](lesson.py) | [Course home](../../README.md)

## What you will learn

This lesson builds the concepts before asking you to memorize syntax. Read each step, find the matching idea in `lesson.py`, run it, and change the example.

## Concepts to understand

- **Iteration:** A `for` loop processes iterable items.
- **Branching:** An `if` condition selects which records proceed.
- **Exceptions:** A narrow `except` handles an expected conversion failure.

## Before you begin

Lesson 2; understand lists, strings, and integers.

## Step-by-step walkthrough

1. **Inspect raw values.** The list includes invalid text, as real data often does.

2. **Convert safely.** Attempt `int(value)` and handle the expected `ValueError`.

3. **Apply a rule.** Keep converted values at least 10, distinguishing invalid from below-threshold values.

## Run the Python example

From the repository root, run:

```bash
python 01-python-core/03-control-flow-and-iteration/lesson.py
```

Only values 12 and 19 pass both checks.

## Practice challenge

Count valid, invalid, and below-threshold values separately.

**Checkpoint:** Explain the input, operation, and what the output can and cannot tell you.

## Common mistake to avoid

A broad `except:` can hide programming errors; catch expected exceptions and record rejected rows when appropriate.

## Continue the course

[Next lesson: Functions and modules](../04-functions-and-modules/README.md)
