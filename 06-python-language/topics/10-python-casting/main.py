"""Python casting: independent learner project. See README.md for purpose and use."""

raw = "42"
value = int(raw)
if value < 0:
    raise ValueError("expected a non-negative count")
print(value)
