"""Hierarchical clustering: runnable, self-contained learner project."""

from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler

X = [[1, 2], [1, 3], [8, 8], [9, 8]]
labels = AgglomerativeClustering(n_clusters=2, linkage="ward").fit_predict(StandardScaler().fit_transform(X))
print("cluster labels:", labels.tolist())
