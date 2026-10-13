"""K-nearest neighbors: runnable, self-contained learner project."""

from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

X = [[1, 1], [1, 2], [8, 8], [9, 8]]
y = ["A", "A", "B", "B"]
model = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=1)).fit(X, y)
print("nearby group:", model.predict([[2, 1]])[0])
