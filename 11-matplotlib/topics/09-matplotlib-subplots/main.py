"""Matplotlib subplots: runnable, self-contained learner project."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
import tempfile


fig, axes = plt.subplots(1, 2, figsize=(8, 3))
axes[0].bar(["A", "B"], [4, 7]); axes[0].set(title="Counts")
axes[1].plot([1, 2, 3], [2, 3, 5], marker="o"); axes[1].set(title="Trend")
fig.tight_layout()
plt.show()

output = Path(tempfile.gettempdir()) / "python-course-matplotlib-subplots.png"
plt.savefig(output, dpi=100)
plt.close("all")
print("Saved figure:", output)
