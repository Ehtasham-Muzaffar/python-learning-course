"""Clustering with K-Means: Scale features before K-Means and compare discovered cluster labels with known groups.

Lesson walkthrough:
    1. Load measurements: Fit to feature measurements only, without target labels.
    2. Scale features: Standardize columns to comparable scales before distance calculations.
    3. Fit and inspect: Choose cluster count and seed, then count assigned records; treat the groups as exploratory.

See README.md for concept explanations and a practice task.
"""
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

data = load_iris()
X_scaled = StandardScaler().fit_transform(data.data)
labels = KMeans(n_clusters=3, n_init=10, random_state=42).fit_predict(X_scaled)
print("cluster sizes:", np.bincount(labels))
print("These are exploratory clusters, not ground-truth class predictions.")
