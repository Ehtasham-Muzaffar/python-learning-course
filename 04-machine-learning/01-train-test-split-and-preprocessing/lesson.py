"""Train-test split and preprocessing: Split before fitting and keep scaling inside a Scikit-Learn pipeline to avoid leakage.

Lesson walkthrough:
    1. Separate features and target: Iris measurements are inputs and species is the target.
    2. Split before fitting: A stratified split preserves class proportions and a seed makes the example repeatable.
    3. Fit pipeline: Scaler learns from training data, then logistic regression fits transformed features.

See README.md for concept explanations and a practice task.
"""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.25, random_state=42, stratify=data.target)
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=500))
model.fit(X_train, y_train)
print("test accuracy:", model.score(X_test, y_test))
