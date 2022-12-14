import tree

# This is an input class. Do not edit.

# This is an input class. Do not edit.


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(node):
    def traverse(node):
        if node is None:
            return [0, 0]
        l, r = traverse(node.left), traverse(node.right)
        maxTotal = max(max(l[1], r[1]), l[0]+r[0])
        return [max(l[0], r[0]) + 1, maxTotal]
    return traverse(node)[1]


bst = tree.BST(5).insert(2).insert(1).insert(3).insert(8)

# bst.traverse()

print(binaryTreeDiameter(bst))
