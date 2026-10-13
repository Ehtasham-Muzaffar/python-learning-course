"""Matplotlib introduction: runnable, self-contained learner project."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
import tempfile


fig, ax = plt.subplots()
ax.plot([1, 2, 3], [2, 4, 3])
ax.set(title="First figure", xlabel="Observation", ylabel="Value")
plt.show()

output = Path(tempfile.gettempdir()) / "python-course-matplotlib-introduction.png"
plt.savefig(output, dpi=100)
plt.close("all")
print("Saved figure:", output)
