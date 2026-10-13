"""Standard deviation: runnable, self-contained learner project."""

from statistics import stdev, pstdev

measurements = [8, 9, 10, 11, 12]
print("sample standard deviation:", round(stdev(measurements), 3))
print("population standard deviation:", round(pstdev(measurements), 3))
