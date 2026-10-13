"""Python self parameter: independent learner project. See README.md for purpose and use."""

class Greeter:
    def __init__(self, name: str) -> None:
        self.name = name

    def greet(self) -> str:
        return f"Hello, {self.name}"

print(Greeter("Amina").greet())
