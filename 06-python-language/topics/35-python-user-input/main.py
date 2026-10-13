"""Python user input: independent learner project. See README.md for purpose and use."""

raw_input = "25"
age = int(raw_input)
if not 0 <= age <= 120:
    raise ValueError("age is outside the accepted range")
print(age)
