def findClosestValueInBst(tree, target):
    node = tree
    mindiff = float("inf")
    closest = None
    while node:
        diff = abs(target - node.value)
        if diff < mindiff:
            mindiff = diff
            closest = node.value
        if target == node.value:
            return node.value
        elif target < node.value:
            node = node.left
        else:
            node = node.right
    return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


tree = BST(10)
tree.right = BST(15)
tree.right.left = BST(13)
tree.right.right = BST(22)
tree.right.left.right = BST(14)
tree.left = BST(5)
tree.left.right = BST(5)
tree.left.left = BST(2)
tree.left.left.left = BST(1)

print(findClosestValueInBst(tree, 6))
