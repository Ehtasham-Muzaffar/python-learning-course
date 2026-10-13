"""Control flow and iteration: Filter records with conditions and safely handle invalid values while iterating.

Lesson walkthrough:
    1. Inspect raw values: The list includes invalid text, as real data often does.
    2. Convert safely: Attempt `int(value)` and handle the expected `ValueError`.
    3. Apply a rule: Keep converted values at least 10, distinguishing invalid from below-threshold values.

See README.md for concept explanations and a practice task.
"""
raw_values = ["12", "7", "unknown", "19"]
valid = []
for value in raw_values:
    try:
        number = int(value)
    except ValueError:
        continue
    if number >= 10:
        valid.append(number)
print("Values at least 10:", valid)
