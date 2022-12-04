def findClosestValueInBst(tree, target):
    if target == tree.value:
        return target

    pass


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


tree = BST(10)
tree.right = BST(15)
tree.right.left = BST(13)
tree.right.left = BST(22)
tree.right.left.right = BST(14)
tree.left = BST(5)
tree.left.right = BST(5)
tree.left.left = BST(2)
tree.left.left.left = BST(1)

print(findClosestValueInBst(tree, 13))
