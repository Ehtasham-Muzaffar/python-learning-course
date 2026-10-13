"""Queues: standalone educational project."""

from collections import deque

queue = deque(["first", "second"])
queue.append("third")
print("next task:", queue.popleft())
print("waiting:", list(queue))
