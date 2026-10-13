"""Python virtual environments: independent learner project. See README.md for purpose and use."""

import sys

print("executable:", sys.executable)
print("prefix:", sys.prefix)
print("base prefix:", sys.base_prefix)
print("venv active:", sys.prefix != sys.base_prefix)
