"""Python match: independent learner project. See README.md for purpose and use."""

command = ("predict", {"rows": 4})
match command:
    case ("predict", {"rows": rows}) if rows > 0:
        print(f"Predict {rows} rows")
    case _:
        print("Unsupported command")
