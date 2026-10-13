"""NumPy arrays: Create and reshape NumPy arrays, then compute vectorized descriptive statistics.

Lesson walkthrough:
    1. Build a 2D array: Represent two observations and three score columns.
    2. Inspect dimensions: Check `.shape` before calculation.
    3. Reduce and broadcast: Calculate column means and divide each row by its maximum using `keepdims=True`.

See README.md for concept explanations and a practice task.
"""
import numpy as np

scores = np.array([[88, 94, 91], [76, 85, 90]], dtype=float)
print("shape:", scores.shape)
print("column means:", scores.mean(axis=0))
print("normalized rows:", scores / scores.max(axis=1, keepdims=True))
