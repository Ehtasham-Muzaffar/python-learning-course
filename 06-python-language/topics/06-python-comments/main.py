"""Python comments: independent learner project. See README.md for purpose and use."""

def average(values: list[float]) -> float:
    """Return the mean of a non-empty numeric sequence."""
    # Reject invalid input before division.
    if not values:
        raise ValueError("values cannot be empty")
    return sum(values) / len(values)

print(average([80, 90, 100]))
