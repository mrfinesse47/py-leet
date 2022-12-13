
def nodeDepths(node, depth=0):
    if node is None:
        return 0
    return nodeDepths(node.left, depth+1) + nodeDepths(node.right, depth + 1) + depth


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
