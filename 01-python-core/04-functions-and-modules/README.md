# Functions and modules

> **Phase 1: Modern Python Core | Lesson 04 of 5** | Beginner | 25 minutes

Write a typed reusable function with a documented input and output contract.

**Keywords:** Python functions, type hints, modular code.

[Phase guide](../README.md) | [Runnable Python script](lesson.py) | [Course home](../../README.md)

## What you will learn

This lesson builds the concepts before asking you to memorize syntax. Read each step, find the matching idea in `lesson.py`, run it, and change the example.

## Concepts to understand

- **Function contract:** Name, parameters, result, and errors describe how callers use code.
- **Type hints:** Annotations document intended types and improve editor support but are not runtime validation.
- **Preconditions:** Early checks provide clear errors.

## Before you begin

Lessons 2?3; understand lists, numbers, and conditions.

## Step-by-step walkthrough

1. **Define the interface.** `mean` accepts a list and returns a reusable value.

2. **Document intent.** Use a docstring and type annotations to communicate the contract.

3. **Handle empty input.** Raise `ValueError`; an empty list has no arithmetic mean.

## Run the Python example

From the repository root, run:

```bash
python 01-python-core/04-functions-and-modules/lesson.py
```

The example prints 91.0; an empty input raises `ValueError`.

## Practice challenge

Implement a median function for odd/even lists and reject empty input.

**Checkpoint:** Explain the input, operation, and what the output can and cannot tell you.

## Common mistake to avoid

Type hints do not validate input at runtime. Reusable calculations should return values rather than print.

## Continue the course

[Next lesson: Classes and object-oriented Python](../05-classes-and-oop/README.md)
