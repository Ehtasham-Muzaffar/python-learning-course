"""K-means clustering: runnable, self-contained learner project."""

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

X = [[1, 2], [1, 3], [8, 8], [9, 8]]
labels = KMeans(n_clusters=2, n_init=10, random_state=42).fit_predict(StandardScaler().fit_transform(X))
print("cluster assignments:", labels.tolist())
