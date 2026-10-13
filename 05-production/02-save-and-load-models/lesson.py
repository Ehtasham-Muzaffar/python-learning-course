"""Save and load models with Joblib: Persist and reload a fitted Scikit-Learn pipeline, then verify its predictions.

Lesson walkthrough:
    1. Train an estimator: Fit logistic regression on built-in data.
    2. Write temporary artifact: Joblib serializes the fitted object outside the repository.
    3. Reload and verify: Load it and compare predictions on identical example inputs.

See README.md for concept explanations and a practice task.
"""
import tempfile
from pathlib import Path
import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

data = load_iris()
model = LogisticRegression(max_iter=500).fit(data.data, data.target)
with tempfile.TemporaryDirectory() as folder:
    path = Path(folder) / "iris.joblib"
    joblib.dump(model, path)
    restored = joblib.load(path)
    print("prediction before save:", model.predict(data.data[:2]))
    print("prediction after load: ", restored.predict(data.data[:2]))
