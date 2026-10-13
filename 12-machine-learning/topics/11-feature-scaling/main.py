"""Feature scaling: runnable, self-contained learner project."""

from sklearn.preprocessing import StandardScaler

train = [[1, 100], [2, 200], [3, 300]]
scaler = StandardScaler().fit(train)
print("learned means:", scaler.mean_)
print("scaled training:", scaler.transform(train).round(2))
