"""Radix sort: standalone educational project."""

def radix_nonnegative(values):
    result, place = values.copy(), 1
    while max(result, default=0) // place:
        buckets = [[] for _ in range(10)]
        for value in result: buckets[(value // place) % 10].append(value)
        result = [item for bucket in buckets for item in bucket]; place *= 10
    return result
def radix_sort(values):
    negatives = [-x for x in values if x < 0]
    positives = [x for x in values if x >= 0]
    return [-x for x in reversed(radix_nonnegative(negatives))] + radix_nonnegative(positives)
print(radix_sort([23, -5, 4, -12]))
