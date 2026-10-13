"""Classes and object-oriented Python: Encapsulate related data and behavior in a small immutable dataclass.

Lesson walkthrough:
    1. Model a measurement: Group its feature name and numeric reading.
    2. Add behavior: `is_missing` checks the instance using `math.isnan`.
    3. Compare examples: Check an ordinary float and NaN explicitly.

See README.md for concept explanations and a practice task.
"""
from dataclasses import dataclass
from math import isnan

@dataclass(frozen=True)
class Measurement:
    feature: str
    value: float

    def is_missing(self) -> bool:
        return isnan(self.value)

reading = Measurement("temperature", 21.5)
missing_reading = Measurement("temperature", float("nan"))
print(reading, "missing=", reading.is_missing())
print(missing_reading, "missing=", missing_reading.is_missing())
