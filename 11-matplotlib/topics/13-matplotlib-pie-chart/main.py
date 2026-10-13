"""Matplotlib pie chart: runnable, self-contained learner project."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
import tempfile


fig, ax = plt.subplots()
ax.pie([50, 30, 20], labels=["A", "B", "C"], autopct="%1.0f%%", startangle=90)
ax.set_title("Parts of one whole")
plt.show()

output = Path(tempfile.gettempdir()) / "python-course-matplotlib-pie-chart.png"
plt.savefig(output, dpi=100)
plt.close("all")
print("Saved figure:", output)
