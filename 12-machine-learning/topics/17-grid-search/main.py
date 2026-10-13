"""Grid search: runnable, self-contained learner project."""

from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier

search = GridSearchCV(DecisionTreeClassifier(random_state=0), {"max_depth": [1, 2, 3]}, cv=3)
search.fit([[0], [1], [2], [3], [4], [5]], [0, 0, 0, 1, 1, 1])
print("best parameter:", search.best_params_)
