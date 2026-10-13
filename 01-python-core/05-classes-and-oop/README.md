# Classes and object-oriented Python

> **Phase 1: Modern Python Core | Lesson 05 of 5** | Beginner | 30 minutes

Encapsulate related data and behavior in a small immutable dataclass.

**Keywords:** Python OOP, classes, dataclasses.

[Phase guide](../README.md) | [Runnable Python script](lesson.py) | [Course home](../../README.md)

## What you will learn

This lesson builds the concepts before asking you to memorize syntax. Read each step, find the matching idea in `lesson.py`, run it, and change the example.

## Concepts to understand

- **Class and instance:** A class defines structure; an instance contains object values.
- **Dataclass:** `@dataclass` generates helpful methods from declared fields.
- **Immutability:** `frozen=True` prevents reassignment after creation.

## Before you begin

Lessons 2?4; understand attributes, functions, and type hints.

## Step-by-step walkthrough

1. **Model a measurement.** Group its feature name and numeric reading.

2. **Add behavior.** `is_missing` checks the instance using `math.isnan`.

3. **Compare examples.** Check an ordinary float and NaN explicitly.

## Run the Python example

From the repository root, run:

```bash
python 01-python-core/05-classes-and-oop/lesson.py
```

The ordinary reading is not missing; NaN reports missing.

## Practice challenge

Add a unit and a Celsius-to-Fahrenheit method without mutation.

**Checkpoint:** Explain the input, operation, and what the output can and cannot tell you.

## Common mistake to avoid

NaN is unequal to itself; use `math.isnan` for scalar floating-point values.

## Continue the course

[Next phase: Phase 2: Data Manipulation and Analysis](../../02-data-analysis/README.md)
