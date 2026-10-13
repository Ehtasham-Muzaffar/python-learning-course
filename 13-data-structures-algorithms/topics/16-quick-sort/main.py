"""Quick sort: standalone educational project."""

def quick_sort(values):
    if len(values) < 2: return values.copy()
    pivot = values[len(values)//2]
    return quick_sort([x for x in values if x < pivot]) + [x for x in values if x == pivot] + quick_sort([x for x in values if x > pivot])
print(quick_sort([5, 1, 4, 2, 2]))
