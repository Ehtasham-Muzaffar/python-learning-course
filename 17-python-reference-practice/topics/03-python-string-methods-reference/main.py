"""Python string methods reference: standalone reference and practice project."""

raw = "  Data Science,Python  "
clean = raw.strip().casefold()
print(clean.split(","))
print(clean.replace("python", "Python"))
