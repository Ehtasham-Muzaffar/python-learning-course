"""Matplotlib bar chart: runnable, self-contained learner project."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
import tempfile


fig, ax = plt.subplots()
ax.bar(["Python", "SQL", "R"], [18, 12, 8], color="steelblue")
ax.set(title="Example survey counts", xlabel="Skill", ylabel="Responses", ylim=(0, 20))
plt.show()

output = Path(tempfile.gettempdir()) / "python-course-matplotlib-bar-chart.png"
plt.savefig(output, dpi=100)
plt.close("all")
print("Saved figure:", output)
