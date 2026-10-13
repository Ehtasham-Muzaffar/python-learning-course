"""Trees: standalone educational project."""

tree = {"root": ["documents", "images"], "documents": ["report.txt"], "images": []}
def visit(node: str) -> None:
    print(node)
    for child in tree.get(node, []):
        visit(child)
visit("root")
