"""Environment and first program: Create a Python virtual environment, inspect the interpreter, and run a reproducible first program.

Lesson walkthrough:
    1. Check Python: Run `python --version` and `python -c "import sys; print(sys.executable)"` to see your shell interpreter.
    2. Isolate packages: Create `.venv` with `python -m venv .venv` and activate it using the root quickstart.
    3. Verify the lesson: Run the script and compare its interpreter path with your active environment.

See README.md for concept explanations and a practice task.
"""
import sys

print(f"Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
print(f"Executable: {sys.executable}")
