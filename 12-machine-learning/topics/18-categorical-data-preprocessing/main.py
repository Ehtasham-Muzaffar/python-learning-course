"""Categorical data preprocessing: runnable, self-contained learner project."""

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

rows = [["north", 18], ["south", 42], ["west", 27]]
prep = ColumnTransformer([("region", OneHotEncoder(handle_unknown="ignore"), [0]), ("age", StandardScaler(), [1])])
print("encoded features:", prep.fit_transform(rows).shape)
