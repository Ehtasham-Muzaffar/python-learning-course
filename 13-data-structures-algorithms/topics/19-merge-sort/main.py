"""Merge sort: standalone educational project."""

def merge_sort(values):
    if len(values) < 2: return values.copy()
    middle = len(values)//2; left=merge_sort(values[:middle]); right=merge_sort(values[middle:])
    merged=[]; i=j=0
    while i<len(left) and j<len(right):
        if left[i] <= right[j]: merged.append(left[i]); i+=1
        else: merged.append(right[j]); j+=1
    return merged + left[i:] + right[j:]
print(merge_sort([5, 1, 4, 2]))
