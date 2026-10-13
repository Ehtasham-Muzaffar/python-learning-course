"""Python practice problems: standalone reference and practice project."""

def second_largest(values: list[int]) -> int:
    unique = sorted(set(values))
    if len(unique) < 2:
        raise ValueError("need two distinct numbers")
    return unique[-2]

print(second_largest([4, 9, 2, 9, 7]))
