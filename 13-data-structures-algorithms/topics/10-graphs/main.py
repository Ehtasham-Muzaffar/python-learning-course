"""Graphs: standalone educational project."""

graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
from collections import deque
queue, seen = deque(["A"]), set()
while queue:
    node = queue.popleft()
    if node not in seen:
        seen.add(node); queue.extend(graph[node])
print("reachable:", sorted(seen))
