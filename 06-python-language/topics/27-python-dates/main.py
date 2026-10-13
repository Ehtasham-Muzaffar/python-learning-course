"""Python dates: independent learner project. See README.md for purpose and use."""

from datetime import datetime, timezone

now = datetime.now(timezone.utc)
print(now.isoformat())
