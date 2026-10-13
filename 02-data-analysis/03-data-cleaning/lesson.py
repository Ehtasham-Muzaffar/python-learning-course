"""Data cleaning: Handle missing values, duplicate rows, and explicit Pandas dtypes in a small dataset.

Lesson walkthrough:
    1. Inspect the sample: Review the missing age and repeated observation.
    2. Remove a true duplicate: Use `drop_duplicates` and copy the working table.
    3. Impute and validate: Fill this example with the median, cast the type, then inspect results.

See README.md for concept explanations and a practice task.
"""
import pandas as pd

raw = pd.DataFrame({"age": [25, None, 25], "city": ["Lahore", "Karachi", "Lahore"]})
clean = raw.drop_duplicates().copy()
clean["age"] = clean["age"].fillna(clean["age"].median()).astype("int64")
print(clean)
print(clean.dtypes)
