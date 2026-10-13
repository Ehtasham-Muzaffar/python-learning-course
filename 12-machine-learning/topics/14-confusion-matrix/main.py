"""Confusion matrix: runnable, self-contained learner project."""

from sklearn.metrics import confusion_matrix, classification_report

actual = [0, 0, 0, 1, 1, 1]
predicted = [0, 1, 0, 1, 0, 1]
print(confusion_matrix(actual, predicted, labels=[0, 1]))
print(classification_report(actual, predicted, zero_division=0))
