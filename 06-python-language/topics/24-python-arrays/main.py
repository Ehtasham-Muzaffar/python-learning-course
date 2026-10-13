"""Python arrays: independent learner project. See README.md for purpose and use."""

from array import array

measurements = array("d", [1.5, 2.0, 3.25])
print("values:", measurements.tolist())
print("type code:", measurements.typecode)
