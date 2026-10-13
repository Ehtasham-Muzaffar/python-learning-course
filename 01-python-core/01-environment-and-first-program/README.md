# Environment and first program

> **Phase 1: Modern Python Core | Lesson 01 of 5** | Beginner | 20 minutes

Create a Python virtual environment, inspect the interpreter, and run a reproducible first program.

**Keywords:** Python setup, virtual environment, Python course.

[Phase guide](../README.md) | [Runnable Python script](lesson.py) | [Course home](../../README.md)

## What you will learn

This lesson builds the concepts before asking you to memorize syntax. Read each step, find the matching idea in `lesson.py`, run it, and change the example.

## Concepts to understand

- **Interpreter:** The program that executes Python source.
- **Virtual environment:** A project-local package space isolated from other projects.
- **Working directory:** The directory from which relative paths are evaluated.

## Before you begin

Python 3.11+ installed; no prior Python experience.

## Step-by-step walkthrough

1. **Check Python.** Run `python --version` and `python -c "import sys; print(sys.executable)"` to see your shell interpreter.

2. **Isolate packages.** Create `.venv` with `python -m venv .venv` and activate it using the root quickstart.

3. **Verify the lesson.** Run the script and compare its interpreter path with your active environment.

## Run the Python example

From the repository root, run:

```bash
python 01-python-core/01-environment-and-first-program/lesson.py
```

Expect your Python version and full interpreter path.

## Practice challenge

Create a temporary second environment and compare `sys.executable` before and after activation.

**Checkpoint:** Explain the input, operation, and what the output can and cannot tell you.

## Common mistake to avoid

A virtual environment does not activate itself; verify the interpreter when packages appear missing.

## Continue the course

[Next lesson: Types and data structures](../02-types-and-data-structures/README.md)
