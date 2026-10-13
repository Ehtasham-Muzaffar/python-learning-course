"""Python OOP: independent learner project. See README.md for purpose and use."""

class Counter:
    def __init__(self, start: int = 0) -> None:
        self.value = start

    def increment(self) -> int:
        self.value += 1
        return self.value

print(Counter().increment())
