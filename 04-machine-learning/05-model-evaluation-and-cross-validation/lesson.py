"""Model evaluation and cross-validation: Estimate classifier performance with stratified cross-validation and inspect multiple metrics.

Lesson walkthrough:
    1. Choose model and metrics: The pipeline keeps scaling inside each fold and computes three complementary metrics.
    2. Define folds: Shuffling and a seed make the demonstration repeatable.
    3. Inspect fold scores: `cross_validate` returns per-fold scores; average them as a compact summary.

See README.md for concept explanations and a practice task.
"""
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_validate, StratifiedKFold
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

data = load_breast_cancer()
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
result = cross_validate(model, data.data, data.target, cv=cv, scoring=["accuracy", "precision", "recall"])
print({metric: result[f"test_{metric}"].mean().round(3) for metric in ("accuracy", "precision", "recall")})
