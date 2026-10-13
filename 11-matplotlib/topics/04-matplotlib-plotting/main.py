"""Matplotlib plotting: runnable, self-contained learner project."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
import tempfile


fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [2, 5, 4, 8], label="series A")
ax.legend()
ax.set(title="Ordered observations", xlabel="Step", ylabel="Measurement")
plt.show()

output = Path(tempfile.gettempdir()) / "python-course-matplotlib-plotting.png"
plt.savefig(output, dpi=100)
plt.close("all")
print("Saved figure:", output)
