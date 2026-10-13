"""Python booleans: independent learner project. See README.md for purpose and use."""

age = 22
has_consent = True
can_register = age >= 18 and has_consent
print(can_register)
