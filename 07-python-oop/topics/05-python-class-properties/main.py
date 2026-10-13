"""Python class properties: independent learner project. See README.md for purpose and use."""

class Celsius:
    def __init__(self, value: float) -> None:
        self.value = value

    @property
    def fahrenheit(self) -> float:
        return self.value * 9 / 5 + 32

print(Celsius(20).fahrenheit)
