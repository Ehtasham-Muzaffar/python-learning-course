"""Vectorization and feature preparation: Use vectorized column operations to create a feature without a Python row loop.

Lesson walkthrough:
    1. Inspect inputs: Each row has numeric quantity and unit price.
    2. Build a vectorized feature: Multiply aligned Series to create the per-row total without a row loop.
    3. Encode a decision: Compare totals against a threshold to create an order-size flag.

See README.md for concept explanations and a practice task.
"""
import pandas as pd

frame = pd.DataFrame({"quantity": [2, 5, 3], "unit_price": [4.5, 2.0, 8.0]})
frame["total"] = frame["quantity"] * frame["unit_price"]
frame["large_order"] = frame["total"] >= 15
print(frame)
