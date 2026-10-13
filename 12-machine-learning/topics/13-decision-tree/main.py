"""Decision tree: runnable, self-contained learner project."""

from sklearn.tree import DecisionTreeClassifier

X = [[0], [1], [2], [3], [4], [5]]
y = ["low", "low", "low", "high", "high", "high"]
model = DecisionTreeClassifier(max_depth=2, random_state=42).fit(X, y)
print("predictions:", model.predict([[1], [4]]).tolist())
print("depth:", model.get_depth())
