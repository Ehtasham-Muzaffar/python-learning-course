"""Python file methods reference: standalone reference and practice project."""

from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    path = Path(folder) / "example.txt"
    path.write_text("one\ntwo\n", encoding="utf-8")
    with path.open(encoding="utf-8") as stream:
        print([line.rstrip() for line in stream])
