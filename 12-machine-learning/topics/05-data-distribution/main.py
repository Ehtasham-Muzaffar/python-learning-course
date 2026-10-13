"""Data distribution: runnable, self-contained learner project."""

import numpy as np

values = np.array([10, 11, 11, 12, 13, 80])
print("min/median/max:", values.min(), np.median(values), values.max())
print("quantiles:", np.quantile(values, [0.25, 0.5, 0.75]))
