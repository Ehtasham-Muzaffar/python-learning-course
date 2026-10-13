"""Matplotlib setup: runnable, self-contained learner project."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
import tempfile

import matplotlib
matplotlib.use("Agg")  # Use before importing pyplot for headless exports.

fig, ax = plt.subplots()
ax.plot([0, 1], [0, 1])
fig.savefig("matplotlib-setup.png")
plt.close(fig)
print("Saved matplotlib-setup.png")

output = Path(tempfile.gettempdir()) / "python-course-matplotlib-setup.png"
plt.savefig(output, dpi=100)
plt.close("all")
print("Saved figure:", output)
