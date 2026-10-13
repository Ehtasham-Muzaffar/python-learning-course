"""Python regular expressions: independent learner project. See README.md for purpose and use."""

import re

text = "order-2026-104"
match = re.fullmatch(r"order-(\d{4})-(\d+)", text)
if match:
    print("year:", match.group(1), "id:", match.group(2))
