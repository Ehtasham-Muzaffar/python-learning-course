"""Python polymorphism: independent learner project. See README.md for purpose and use."""

class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return 3.14159 * self.radius**2

shapes = [Circle(1), Circle(2)]
print([round(shape.area(), 2) for shape in shapes])
