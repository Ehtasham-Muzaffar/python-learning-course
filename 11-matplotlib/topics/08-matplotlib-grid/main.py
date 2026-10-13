"""Matplotlib grid: runnable, self-contained learner project."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
import tempfile


fig, ax = plt.subplots()
ax.plot([1, 2, 3], [3, 5, 4], marker="o")
ax.grid(axis="y", alpha=0.25)
ax.set(title="Subtle comparison grid", ylabel="Value")
plt.show()

output = Path(tempfile.gettempdir()) / "python-course-matplotlib-grid.png"
plt.savefig(output, dpi=100)
plt.close("all")
print("Saved figure:", output)
