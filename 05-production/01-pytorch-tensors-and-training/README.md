# PyTorch tensors and training

> **Phase 5: Deep Learning and Production Basics | Lesson 01 of 5** | Intermediate | 40 minutes

Run a tiny PyTorch regression training loop and observe the loss decrease.

**Keywords:** PyTorch for beginners, deep learning, tensors.

[Phase guide](../README.md) | [Runnable Python script](lesson.py) | [Course home](../../README.md)

## What you will learn

Build the concepts before memorizing syntax. Read each step, find the matching idea in `lesson.py`, run it, and change the example.

## Concepts to understand

- **Tensor:** A multidimensional value whose operations can be tracked for automatic differentiation.
- **Loss:** Mean squared error measures prediction differences from targets.
- **Training loop:** Predict, calculate loss, clear gradients, backpropagate, and update parameters.

## Before you begin

Linear regression, derivative intuition, and optional PyTorch dependencies. Install the optional stack with `python -m pip install -r requirements-deep-learning.txt`.

## Step-by-step walkthrough

1. **Create known data.** Use `y = 2x + 1` so expected parameters are known.

2. **Initialize learnable model.** `torch.nn.Linear` creates parameters; SGD applies gradient updates.

3. **Repeat optimization.** Compute loss, zero gradients, call `backward`, and step the optimizer.

## Run the Python example

From the repository root, run:

```bash
python 05-production/01-pytorch-tensors-and-training/lesson.py
```

Loss should decrease; fitted weight and bias should approach 2 and 1.

## Practice challenge

Print initial and final parameters; experiment with learning rate after resetting the seed.

**Checkpoint:** Explain the input, operation, and what the output can and cannot tell you.

## Common mistake to avoid

A real training system also needs validation, data batching, and monitoring; follow operation order in the loop.

## Continue the course

[Next lesson: Save and load models with Joblib](../02-save-and-load-models/README.md)
