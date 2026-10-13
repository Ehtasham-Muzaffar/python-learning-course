"""Python class methods: independent learner project. See README.md for purpose and use."""

class Celsius:
    def __init__(self, value: float) -> None:
        self.value = value

    @classmethod
    def from_fahrenheit(cls, value: float) -> "Celsius":
        return cls((value - 32) * 5 / 9)

print(Celsius.from_fahrenheit(68).value)
