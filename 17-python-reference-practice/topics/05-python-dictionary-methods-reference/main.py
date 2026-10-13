"""Python dictionary methods reference: standalone reference and practice project."""

record = {"name": "Amina", "score": 91}
print(record.get("age", "not supplied"))
for key, value in record.items():
    print(key, value)
