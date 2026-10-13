"""Seaborn statistical plots: Compare distributions across categories with a labeled Seaborn box plot.

Lesson walkthrough:
    1. Inspect tidy sample: The script builds an offline category and bill-value table.
    2. Map fields: Put category on x and numeric measurements on y to compare groups.
    3. Label and compare: Look at medians, spread, and group sizes before interpreting differences.

See README.md for concept explanations and a practice task.
"""
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

frame = pd.DataFrame(
    {
        "day": ["Mon", "Mon", "Tue", "Tue", "Wed", "Wed", "Thu", "Thu"],
        "total_bill": [18, 24, 15, 21, 22, 29, 17, 25],
    }
)
ax = sns.boxplot(data=frame, x="day", y="total_bill", hue="day", legend=False)
ax.set(title="Example bill by day", xlabel="Day", ylabel="Total bill")
plt.tight_layout()
plt.show()
