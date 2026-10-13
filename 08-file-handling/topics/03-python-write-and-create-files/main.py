"""Python write and create files: independent learner project. See README.md for purpose and use."""

from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    path = Path(folder) / "report.txt"
    path.write_text("report\n", encoding="utf-8")
    with path.open("a", encoding="utf-8") as file:
        file.write("complete\n")
    print(path.read_text(encoding="utf-8"))
