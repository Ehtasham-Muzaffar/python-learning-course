"""Python inner classes: independent learner project. See README.md for purpose and use."""

class Table:
    class Column:
        def __init__(self, name: str) -> None:
            self.name = name

column = Table.Column("score")
print(column.name)
