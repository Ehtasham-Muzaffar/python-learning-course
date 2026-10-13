"""Percentiles: runnable, self-contained learner project."""

import numpy as np

latencies_ms = np.array([10, 12, 15, 18, 40])
print("median:", np.percentile(latencies_ms, 50))
print("90th percentile:", np.percentile(latencies_ms, 90))
