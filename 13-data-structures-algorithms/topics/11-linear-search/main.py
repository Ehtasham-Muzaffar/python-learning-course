"""Linear search: standalone educational project."""

def linear_search(values, target):
    for index, value in enumerate(values):
        if value == target: return index
    return -1
print(linear_search([8, 3, 5], 5))
