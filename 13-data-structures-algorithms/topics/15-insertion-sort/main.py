"""Insertion sort: standalone educational project."""

def insertion_sort(values):
    result = values.copy()
    for i in range(1, len(result)):
        current, position = result[i], i
        while position and result[position-1] > current:
            result[position] = result[position-1]; position -= 1
        result[position] = current
    return result
print(insertion_sort([5, 1, 4, 2]))
