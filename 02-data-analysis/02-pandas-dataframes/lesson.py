"""Pandas DataFrames: Inspect, filter, and aggregate tabular records with Pandas.

Lesson walkthrough:
    1. Build a table: Each row is a team observation; column lengths must agree.
    2. Filter: Use a score comparison as a Boolean mask.
    3. Aggregate: Group hours by team, calculate the mean, and keep the team key as a column.

See README.md for concept explanations and a practice task.
"""
import pandas as pd

frame = pd.DataFrame({"team": ["A", "A", "B"], "hours": [3.0, 5.0, 4.0], "score": [80, 92, 88]})
print(frame[frame["score"] >= 85])
print(frame.groupby("team", as_index=False)["hours"].mean())
