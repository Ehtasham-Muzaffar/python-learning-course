"""AVL trees: standalone educational project."""

class Node:
    def __init__(self, value): self.value, self.left, self.right, self.height = value, None, None, 1
def height(node): return node.height if node else 0
def rotate_right(root):
    pivot = root.left
    root.left = pivot.right; pivot.right = root
    root.height = 1 + max(height(root.left), height(root.right))
    pivot.height = 1 + max(height(pivot.left), height(pivot.right))
    return pivot
root = Node(30); root.left = Node(20); root.left.left = Node(10)
root = rotate_right(root)
print("balanced root:", root.value, "height:", root.height)
