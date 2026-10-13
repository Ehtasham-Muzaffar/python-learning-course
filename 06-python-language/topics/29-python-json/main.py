"""Python JSON: independent learner project. See README.md for purpose and use."""

import json

record = {"name": "Amina", "score": 91}
text = json.dumps(record)
restored = json.loads(text)
print(restored["name"], restored["score"])
