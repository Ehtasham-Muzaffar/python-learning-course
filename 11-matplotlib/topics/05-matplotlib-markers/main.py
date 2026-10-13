"""Matplotlib markers: runnable, self-contained learner project."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
import tempfile


fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 2, 5], marker="o", markersize=8)
ax.set(title="Measurements and points", xlabel="Sample", ylabel="Value")
plt.show()

output = Path(tempfile.gettempdir()) / "python-course-matplotlib-markers.png"
plt.savefig(output, dpi=100)
plt.close("all")
print("Saved figure:", output)
