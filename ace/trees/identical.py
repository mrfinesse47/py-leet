# Importing required functions
from binary_tree import *
from binary_tree_node import *


def are_identical(root1, root2):
    isEqual = True

    def dfs(root1, root2):
        nonlocal isEqual
        if root1 is None and root2 is None:
            return
        elif root1 is None:
            isEqual = False
            return
        elif root2 is None:
            isEqual = False
            return
        else:
            dfs(root1.left, root2.left)
            if root1.data != root2.data:
                isEqual = False
                return
            dfs(root1.right, root2.right)
    dfs(root1, root2)
    return isEqual


def are_identical(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif root1 is None or root2 is None:
        return False
    else:
        return False if are_identical(root1.left, root2.left) == False or are_identical(root1.right, root2.right) == False or root1.data != root2.data else True


root1 = BinaryTree()
root1.insert_List([25, 50, 100, 125, 200, 350, 400])
root2 = BinaryTree()
root2.insert_List([25, 50, 100, 125, 200, 350, 400])

print(are_identical(root1.root, root2.root))
