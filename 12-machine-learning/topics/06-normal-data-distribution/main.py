"""Normal data distribution: runnable, self-contained learner project."""

import numpy as np

rng = np.random.default_rng(42)
sample = rng.normal(loc=10, scale=2, size=1000)
print("sample mean/std:", round(sample.mean(), 2), round(sample.std(ddof=1), 2))
print("approx within 2 std:", np.mean(np.abs(sample - sample.mean()) <= 2 * sample.std()))
