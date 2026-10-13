"""Python exceptions reference: standalone reference and practice project."""

try:
    int("12.5")
except ValueError as error:
    print("integer conversion failed:", error.__class__.__name__)
