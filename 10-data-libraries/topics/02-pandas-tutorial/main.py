"""Pandas tutorial: independent learner project. See README.md for purpose and use."""

import pandas as pd

frame = pd.DataFrame({"team": ["A", "A", "B"], "score": [80, 90, 85]})
print(frame.groupby("team", as_index=False)["score"].mean())
