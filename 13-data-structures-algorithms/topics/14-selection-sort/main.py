"""Selection sort: standalone educational project."""

def selection_sort(values):
    result = values.copy()
    for start in range(len(result)):
        smallest = min(range(start, len(result)), key=result.__getitem__)
        result[start], result[smallest] = result[smallest], result[start]
    return result
print(selection_sort([5, 1, 4, 2]))
