"""Matplotlib scatter plot: runnable, self-contained learner project."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
import tempfile


x = [1, 2, 3, 4]
y = [2, 2.5, 4, 3.8]
fig, ax = plt.subplots()
ax.scatter(x, y, alpha=0.8)
ax.set(title="Two measurements", xlabel="Input", ylabel="Output")
plt.show()

output = Path(tempfile.gettempdir()) / "python-course-matplotlib-scatter-plot.png"
plt.savefig(output, dpi=100)
plt.close("all")
print("Saved figure:", output)
