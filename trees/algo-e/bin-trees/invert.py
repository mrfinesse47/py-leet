import tree


def invertBinaryTree(tree):
    if tree is None:
        return
    tmp = tree.left
    tree.left = tree.right
    tree.right = tmp
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


bst = tree.BST(10).insert(5).insert(5).insert(
    2).insert(1).insert(15).insert(13).insert(14).insert(22)

bst.traverse()

invertBinaryTree(bst)
print("jjjjjjjjjj")

bst.traverse()
