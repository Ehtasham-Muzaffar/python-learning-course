"""Machine learning getting started: runnable, self-contained learner project."""

from sklearn.dummy import DummyClassifier
from sklearn.model_selection import train_test_split

X = [[0], [1], [2], [3], [4], [5]]
y = [0, 0, 0, 1, 1, 1]
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=7)
model = DummyClassifier(strategy="most_frequent").fit(X_train, y_train)
print("baseline accuracy:", model.score(X_test, y_test))
