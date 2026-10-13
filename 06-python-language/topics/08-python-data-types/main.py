"""Python data types: independent learner project. See README.md for purpose and use."""

values = ["data", 42, 3.14, True, None]
for value in values:
    print(repr(value), type(value).__name__)
