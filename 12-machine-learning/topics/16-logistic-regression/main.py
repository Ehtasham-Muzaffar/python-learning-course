"""Logistic regression: runnable, self-contained learner project."""

from sklearn.linear_model import LogisticRegression

X = [[0], [1], [2], [3], [4], [5]]
y = [0, 0, 0, 1, 1, 1]
model = LogisticRegression().fit(X, y)
print("class:", model.predict([[2.5]])[0])
print("probabilities:", model.predict_proba([[2.5]]).round(3))
