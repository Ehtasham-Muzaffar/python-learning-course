"""Matplotlib labels: runnable, self-contained learner project."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
import tempfile


fig, ax = plt.subplots()
ax.plot([1, 2, 3], [5, 7, 6], label="Observed")
ax.set(title="Example readings", xlabel="Trial", ylabel="Reading (units)")
ax.legend(title="Series")
fig.text(0.01, 0.01, "Source: generated teaching data")
plt.show()

output = Path(tempfile.gettempdir()) / "python-course-matplotlib-labels.png"
plt.savefig(output, dpi=100)
plt.close("all")
print("Saved figure:", output)
