"""Cross validation: runnable, self-contained learner project."""

from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.linear_model import LogisticRegression

X = [[0], [1], [2], [3], [4], [5], [6], [7]]
y = [0, 0, 0, 0, 1, 1, 1, 1]
cv = StratifiedKFold(n_splits=4, shuffle=True, random_state=42)
print("fold accuracies:", cross_val_score(LogisticRegression(), X, y, cv=cv).round(2))
