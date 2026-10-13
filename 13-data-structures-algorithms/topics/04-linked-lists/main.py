"""Linked lists: standalone educational project."""

from dataclasses import dataclass

@dataclass
class Node:
    value: int
    next: "Node | None" = None

head = Node(1, Node(2, Node(3)))
current = head
while current:
    print(current.value)
    current = current.next
