from data_structures.node import Node


def tree_height(root: Node | None) -> int:
    if root is None:
        return -1
    
    if root.left is None and root.right is None:
        return 0
    
    left_heigth = tree_height(root.left)
    right_heigth = tree_height(root.right)

    return 1 + max(left_heigth, right_heigth)