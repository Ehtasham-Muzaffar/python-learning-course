"""Counting sort: standalone educational project."""

def counting_sort(values):
    if not values: return []
    low, high = min(values), max(values)
    counts = [0] * (high-low+1)
    for value in values: counts[value-low] += 1
    return [value for value, count in enumerate(counts, low) for _ in range(count)]
print(counting_sort([4, -1, 2, 4]))
