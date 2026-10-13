"""Python sets: independent learner project. See README.md for purpose and use."""

left = {"python", "numpy", "pandas"}
right = {"pandas", "sklearn"}
print("shared:", left & right)
print("all unique:", left | right)
