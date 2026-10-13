# ONNX model export

> **Phase 5: Deep Learning and Production Basics | Lesson 03 of 5** | Intermediate | 45 minutes

Identify the ONNX conversion and runtime steps while keeping optional dependencies out of the core install.

**Keywords:** ONNX, model deployment, interoperable machine learning.

[Phase guide](../README.md) | [Runnable Python script](lesson.py) | [Course home](../../README.md)

## What you will learn

Build the concepts before memorizing syntax. Read each step, find the matching idea in `lesson.py`, run it, and change the example.

## Concepts to understand

- **ONNX:** An open representation for exchanging models across supported runtimes.
- **Conversion:** A converter maps an estimator to graph operators; support is not universal.
- **Runtime validation:** Run the graph and compare outputs against the source estimator.

## Before you begin

Scikit-Learn LogisticRegression, NumPy arrays, and optional ONNX dependencies. Install the optional stack with `python -m pip install -r requirements-deep-learning.txt`.

## Step-by-step walkthrough

1. **Fit source model.** Train LogisticRegression and note the input feature count.

2. **Convert with signature.** Declare a variable batch dimension and fixed width with `FloatTensorType`.

3. **Run inference.** Use CPU ONNX Runtime, provide float32 features, and inspect output.

## Run the Python example

From the repository root, run:

```bash
python 05-production/03-onnx-model-export/lesson.py
```

The script validates ONNX predictions against the fitted Scikit-Learn model for three Iris rows.

## Practice challenge

Compare converted outputs with original model predictions over representative inputs.

**Checkpoint:** Explain the input, operation, and what the output can and cannot tell you.

## Common mistake to avoid

Validate supported operators, input schema, output shape, and numerical agreement before deployment.

## Continue the course

[Next lesson: FastAPI model service](../04-fastapi-model-service/README.md)
