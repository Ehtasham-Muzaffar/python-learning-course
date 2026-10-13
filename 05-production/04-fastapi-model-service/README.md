# FastAPI model service

> **Phase 5: Deep Learning and Production Basics | Lesson 04 of 5** | Intermediate | 40 minutes

Define a typed FastAPI request and prediction endpoint with explicit input validation.

**Keywords:** FastAPI machine learning API, model serving, REST API.

[Phase guide](../README.md) | [Runnable Python script](lesson.py) | [Course home](../../README.md)

## What you will learn

Build the concepts before memorizing syntax. Read each step, find the matching idea in `lesson.py`, run it, and change the example.

## Concepts to understand

- **Endpoint:** An HTTP method and path identify an operation such as POST `/predict`.
- **Request validation:** Pydantic checks required fields and value bounds.
- **Model serving:** A real service must load a versioned pipeline and validate its feature schema.

## Before you begin

Python functions, type annotations, HTTP basics, and core dependencies.

## Step-by-step walkthrough

1. **Declare input schema.** Require a number between 0 and 100.

2. **Connect schema and route.** FastAPI validates request JSON before calling the handler.

3. **Start locally.** Run `uvicorn lesson:app --reload` in this lesson folder and inspect `/docs`.

## Run the Python example

From the repository root, run:

```bash
python 05-production/04-fastapi-model-service/lesson.py
```

A valid request returns JSON; an out-of-range request receives a validation error.

## Practice challenge

Replace the baseline with a saved model and add an automated request test.

**Checkpoint:** Explain the input, operation, and what the output can and cannot tell you.

## Common mistake to avoid

This unauthenticated local demo is not internet-ready; add security, monitoring, timeouts, and deployment controls.

## Continue the course

[Next lesson: Streamlit model demo](../05-streamlit-model-demo/README.md)
