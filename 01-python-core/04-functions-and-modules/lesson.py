"""Functions and modules: Write a typed reusable function with a documented input and output contract.

Lesson walkthrough:
    1. Define the interface: `mean` accepts a list and returns a reusable value.
    2. Document intent: Use a docstring and type annotations to communicate the contract.
    3. Handle empty input: Raise `ValueError`; an empty list has no arithmetic mean.

See README.md for concept explanations and a practice task.
"""
def mean(values: list[float]) -> float:
    """Return the arithmetic mean of a non-empty list."""
    if not values:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)

print(f"Mean score: {mean([88.0, 94.0, 91.0]):.1f}")
