"""NumPy tutorial: independent learner project. See README.md for purpose and use."""

import numpy as np

values = np.array([[1, 2], [3, 4]], dtype=float)
print("shape:", values.shape)
print("column mean:", values.mean(axis=0))
