"""Python try except: independent learner project. See README.md for purpose and use."""

raw = "not-an-integer"
try:
    value = int(raw)
except ValueError as error:
    print(f"Reject invalid count {raw!r}: {error}")
