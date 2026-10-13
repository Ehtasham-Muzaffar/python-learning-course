"""Classification: Train a classifier and inspect class-wise precision, recall, and confusion counts.

Lesson walkthrough:
    1. Choose target: The built-in dataset has a binary target and readable labels.
    2. Split stratified: Keep approximate class balance in train and test subsets.
    3. Scale, fit, inspect: Use a pipeline then report per-class precision, recall, and F1.

See README.md for concept explanations and a practice task.
"""
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

data = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, stratify=data.target, random_state=42)
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)).fit(X_train, y_train)
print(classification_report(y_test, model.predict(X_test), target_names=data.target_names))
