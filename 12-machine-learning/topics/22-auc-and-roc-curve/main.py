"""AUC and ROC curve: runnable, self-contained learner project."""

from sklearn.metrics import roc_auc_score, roc_curve

actual = [0, 0, 1, 1]
scores = [0.1, 0.6, 0.4, 0.9]
fpr, tpr, thresholds = roc_curve(actual, scores)
print("ROC AUC:", roc_auc_score(actual, scores))
print("FPR/TPR:", fpr.tolist(), tpr.tolist())
