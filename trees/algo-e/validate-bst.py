import tree


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(node, minL=float("-inf"), maxR=float("inf")):
    if node is None:
        return True
    if node.value < minL or node.value >= maxR:
        return False
    return True if validateBst(node.left, minL, node.value) and validateBst(node.right, node.value, maxR) else False


bst = tree.BST(10).insert(5).insert(5).insert(
    2).insert(1).insert(15).insert(13).insert(14).insert(22)

print(validateBst(bst))
# bst.traverse()
