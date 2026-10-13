"""Polynomial regression: runnable, self-contained learner project."""

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

X = [[0], [1], [2], [3], [4]]
y = [1, 2, 5, 10, 17]
model = make_pipeline(PolynomialFeatures(2, include_bias=False), LinearRegression()).fit(X, y)
print("curved prediction at 5:", model.predict([[5]])[0])
