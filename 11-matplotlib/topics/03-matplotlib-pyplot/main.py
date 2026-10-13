"""Matplotlib pyplot: runnable, self-contained learner project."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
import tempfile


plt.plot([1, 2, 3], [1, 4, 9])
plt.title("Stateful pyplot example")
plt.xlabel("Input")
plt.ylabel("Squared value")
plt.show()

output = Path(tempfile.gettempdir()) / "python-course-matplotlib-pyplot.png"
plt.savefig(output, dpi=100)
plt.close("all")
print("Saved figure:", output)
