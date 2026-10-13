"""Python file handling: independent learner project. See README.md for purpose and use."""

from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    path = Path(folder) / "notes.txt"
    with path.open("w", encoding="utf-8") as file:
        file.write("learning Python\n")
    print(path.exists())
