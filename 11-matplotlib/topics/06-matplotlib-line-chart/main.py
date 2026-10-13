"""Matplotlib line chart: runnable, self-contained learner project."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
import tempfile


fig, ax = plt.subplots()
ax.plot(["Jan", "Feb", "Mar"], [12, 15, 11], marker="o")
ax.set(title="Monthly totals", xlabel="Month", ylabel="Units")
plt.show()

output = Path(tempfile.gettempdir()) / "python-course-matplotlib-line-chart.png"
plt.savefig(output, dpi=100)
plt.close("all")
print("Saved figure:", output)
