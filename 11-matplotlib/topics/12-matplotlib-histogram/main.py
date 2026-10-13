"""Matplotlib histogram: runnable, self-contained learner project."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
import tempfile


values = [2, 3, 3, 4, 4, 5, 7, 8, 9]
fig, ax = plt.subplots()
ax.hist(values, bins=5, edgecolor="white")
ax.set(title="Value distribution", xlabel="Value", ylabel="Frequency")
plt.show()

output = Path(tempfile.gettempdir()) / "python-course-matplotlib-histogram.png"
plt.savefig(output, dpi=100)
plt.close("all")
print("Saved figure:", output)
