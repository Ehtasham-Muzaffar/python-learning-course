"""Exploratory data analysis: Combine summary statistics, missingness checks, and distributions in an EDA baseline.

Lesson walkthrough:
    1. Load built-in data: Scikit-Learn supplies Iris locally, avoiding a download.
    2. Check data quality: `describe` summarizes numeric columns and `isna` counts missing values.
    3. Compare groups: Group sepal length by label and treat differences as hypotheses, not causal results.

See README.md for concept explanations and a practice task.
"""
import pandas as pd
from sklearn.datasets import load_iris

data = load_iris(as_frame=True)
frame = data.frame
print(frame.describe().round(2))
print("Missing values:", int(frame.isna().sum().sum()))
print(frame.groupby("target")["sepal length (cm)"].mean().round(2))
