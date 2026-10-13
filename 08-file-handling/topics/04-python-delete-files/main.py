"""Python delete files: independent learner project. See README.md for purpose and use."""

from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    path = Path(folder) / "temporary.txt"
    path.write_text("temporary", encoding="utf-8")
    path.unlink()
    print("exists after delete:", path.exists())
