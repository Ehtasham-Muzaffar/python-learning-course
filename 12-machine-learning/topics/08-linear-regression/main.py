"""Linear regression: runnable, self-contained learner project."""

from sklearn.linear_model import LinearRegression

X = [[1], [2], [3], [4]]
y = [3, 5, 7, 9]
model = LinearRegression().fit(X, y)
print("slope/intercept:", model.coef_[0], model.intercept_)
print("prediction at 5:", model.predict([[5]])[0])
