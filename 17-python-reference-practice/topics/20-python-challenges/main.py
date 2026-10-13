"""Python challenges: standalone reference and practice project."""

def word_count(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for word in text.casefold().split():
        counts[word] = counts.get(word, 0) + 1
    return counts

print(word_count("Python is fun and Python is useful"))
