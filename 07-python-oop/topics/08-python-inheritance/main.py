"""Python inheritance: independent learner project. See README.md for purpose and use."""

class Shape:
    def area(self) -> float:
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width, self.height = width, height

    def area(self) -> float:
        return self.width * self.height

print(Rectangle(3, 4).area())
