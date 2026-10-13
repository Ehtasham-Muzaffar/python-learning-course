"""Python read files: independent learner project. See README.md for purpose and use."""

from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    path = Path(folder) / "input.txt"
    path.write_text("first\nsecond\n", encoding="utf-8")
    with path.open(encoding="utf-8") as source:
        for number, line in enumerate(source, 1):
            print(number, line.rstrip())
