"""Python __init__ method: independent learner project. See README.md for purpose and use."""

class PositiveCount:
    def __init__(self, value: int) -> None:
        if value < 0:
            raise ValueError("count cannot be negative")
        self.value = value

print(PositiveCount(4).value)
