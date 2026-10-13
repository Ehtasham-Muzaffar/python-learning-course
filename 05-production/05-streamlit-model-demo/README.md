# Streamlit model demo

> **Phase 5: Deep Learning and Production Basics | Lesson 05 of 5** | Intermediate | 30 minutes

Build an interactive Streamlit interface around a transparent baseline prediction.

**Keywords:** Streamlit machine learning app, model demo, data app.

[Phase guide](../README.md) | [Runnable Python script](lesson.py) | [Course home](../../README.md)

## What you will learn

Build the concepts before memorizing syntax. Read each step, find the matching idea in `lesson.py`, run it, and change the example.

## Concepts to understand

- **Reactive app:** Streamlit reruns Python as a widget changes.
- **Widget state:** A slider provides bounded user input.
- **Inference interface:** Explain inputs, outputs, assumptions, and model limitations.

## Before you begin

Python functions, prediction basics, and core dependencies.

## Step-by-step walkthrough

1. **Create a clear page.** Set a title describing the demonstration.

2. **Collect input.** The slider constrains the value range and provides a default.

3. **Show a labeled result.** Display the baseline and explain that it is not a trained model.

## Run the Python example

From the repository root, run:

```bash
python 05-production/05-streamlit-model-demo/lesson.py
```

A slider and baseline result appear; changing input updates the displayed value.

## Practice challenge

Load the saved pipeline and replace the baseline with its real prediction.

**Checkpoint:** Explain the input, operation, and what the output can and cannot tell you.

## Common mistake to avoid

Do not present a placeholder formula as a validated model; make limitations and input guidance visible.

## Continue the course

[Back to the course home](../../README.md)
