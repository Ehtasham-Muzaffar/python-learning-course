"""Python remove list duplicates: standalone reference and practice project."""

values = [3, 1, 3, 2, 1]
unique = list(dict.fromkeys(values))
print(unique)
