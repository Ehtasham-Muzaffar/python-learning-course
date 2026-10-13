"""Multiple regression: runnable, self-contained learner project."""

from sklearn.linear_model import LinearRegression

X = [[1, 0], [2, 1], [3, 0], [4, 1]]
y = [4, 8, 8, 12]
model = LinearRegression().fit(X, y)
print("feature coefficients:", model.coef_.round(2))
print("prediction:", model.predict([[5, 1]])[0])
