"""Regression: Fit a baseline regression model and report held-out mean absolute error.

Lesson walkthrough:
    1. Load data: The built-in diabetes dataset contains numeric features and continuous target.
    2. Reserve test observations: Fit only on training records.
    3. Measure predictions: Calculate held-out MAE and retain interpretable target units.

See README.md for concept explanations and a practice task.
"""
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

data = load_diabetes()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, random_state=42)
model = LinearRegression().fit(X_train, y_train)
predictions = model.predict(X_test)
print(f"MAE: {mean_absolute_error(y_test, predictions):.1f} target units")
