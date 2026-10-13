"""Python magic methods: independent learner project. See README.md for purpose and use."""

class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x, self.y = x, y

    def __repr__(self) -> str:
        return f"Point(x={self.x}, y={self.y})"

print(Point(2, 5))
