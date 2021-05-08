class Node:
    def __init__(self, id):
        self.id = id
        self.parent = self
        self.rank = 0
        self.size = 1


def find(x):
    if x.parent is not x:
        x.parent = find(x.parent)

    return x.parent


def union(x, y):
    x_root = find(x)
    y_root = find(y)

    if x_root is y_root:
        return

    if x_root.rank < y_root.rank:
        x_root, y_root = y_root, x_root

    y_root.parent = x_root
    x_root.size += y_root.size
    if x_root.rank == y_root.rank:
        x_root.rank = x_root.rank + 1
