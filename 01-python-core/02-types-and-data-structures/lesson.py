"""Types and data structures: Represent a small dataset with Python strings, numbers, lists, dictionaries, and sets.

Lesson walkthrough:
    1. Inspect a dictionary: The student record groups a name, scores, and an active flag.
    2. Select numeric types: Scores are integers, while a mean may be a float.
    3. Summarize: `sum` and `len` calculate an average; `set` demonstrates uniqueness, not sorting.

See README.md for concept explanations and a practice task.
"""
student = {"name": "Amina", "scores": [88, 94, 91], "active": True}
average = sum(student["scores"]) / len(student["scores"])
print(f"{student['name']}: {average:.1f}; active={student['active']}")
print("Unique scores:", set(student["scores"]))
