"""Train and test split: runnable, self-contained learner project."""

from sklearn.model_selection import train_test_split

X = [[i] for i in range(12)]
y = [i % 2 for i in range(12)]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, stratify=y, random_state=42)
print("train/test sizes:", len(X_train), len(X_test))
print("test labels:", y_test)
