"""Python exercises: standalone reference and practice project."""

def clamp(value: float, low: float, high: float) -> float:
    if low > high:
        raise ValueError("low must not exceed high")
    return min(max(value, low), high)

assert clamp(12, 0, 10) == 10
assert clamp(-1, 0, 10) == 0
print("exercise checks passed")
