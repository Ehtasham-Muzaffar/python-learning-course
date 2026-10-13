"""Hyperparameter tuning: Tune a pipeline with cross-validation and evaluate the selected estimator on held-out data.

Lesson walkthrough:
    1. Hold out final test: Split once so the final score cannot influence model selection.
    2. Declare pipeline and search: Tune SVC parameters with pipeline-qualified names; refit preprocessing per fold.
    3. Evaluate once: Inspect best CV settings, then score selected estimator on test data.

See README.md for concept explanations and a practice task.
"""
from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, stratify=data.target, random_state=42)
search = GridSearchCV(make_pipeline(StandardScaler(), SVC()), {"svc__C": [0.1, 1, 10], "svc__kernel": ["linear", "rbf"]}, cv=5)
search.fit(X_train, y_train)
print("best parameters:", search.best_params_)
print("held-out accuracy:", search.score(X_test, y_test))
