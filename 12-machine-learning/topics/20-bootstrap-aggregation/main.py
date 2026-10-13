"""Bootstrap aggregation: runnable, self-contained learner project."""

from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier

X = [[0], [1], [2], [3], [4], [5]]
y = [0, 0, 0, 1, 1, 1]
model = BaggingClassifier(estimator=DecisionTreeClassifier(), n_estimators=10, random_state=42).fit(X, y)
print("ensemble predictions:", model.predict([[1], [4]]).tolist())
