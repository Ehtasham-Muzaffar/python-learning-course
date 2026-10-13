"""Matplotlib fundamentals: Build a labeled Matplotlib figure and make its visual encodings clear.

Lesson walkthrough:
    1. Define data and question: Four ordered monthly counts make a line chart suitable for highlighting change.
    2. Create explicit axes: `plt.subplots` returns the Figure and Axes so settings are targeted.
    3. Label and render: Add title and units, adjust spacing, then display; `fig.savefig` exports a chart.

See README.md for concept explanations and a practice task.
"""
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
values = [12, 17, 15, 22]
fig, ax = plt.subplots(figsize=(6, 3))
ax.plot(months, values, marker="o")
ax.set(title="Monthly observations", xlabel="Month", ylabel="Count")
fig.tight_layout()
plt.show()
