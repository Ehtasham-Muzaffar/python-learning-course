"""Python set methods reference: standalone reference and practice project."""

required = {"python", "pandas", "numpy"}
known = {"python", "numpy", "sql"}
print("missing:", required.difference(known))
print("shared:", required.intersection(known))
