"""Binary search trees: standalone educational project."""

class Node:
    def __init__(self, value): self.value, self.left, self.right = value, None, None
def insert(node, value):
    if node is None: return Node(value)
    if value < node.value: node.left = insert(node.left, value)
    elif value > node.value: node.right = insert(node.right, value)
    return node
root = None
for value in [5, 3, 7, 4]: root = insert(root, value)
print("root:", root.value, "left child:", root.left.value)
