"""Binary trees: standalone educational project."""

from dataclasses import dataclass

@dataclass
class Node:
    value: int
    left: "Node | None" = None
    right: "Node | None" = None

root = Node(2, Node(1), Node(3))
def inorder(node):
    if node:
        inorder(node.left); print(node.value); inorder(node.right)
inorder(root)
