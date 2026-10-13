"""Machine learning scatter plot: runnable, self-contained learner project."""

import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5]
scores = [52, 61, 65, 78, 82]
fig, ax = plt.subplots()
ax.scatter(hours, scores)
ax.set(xlabel="Study hours", ylabel="Example score", title="Association is not causation")
plt.show()
