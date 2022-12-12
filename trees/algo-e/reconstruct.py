# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(values):
    values.reverse()  # mistake made forgot to reverse for easy pop
    # also could have use an indexer and not have had to reverse the arr
    root = None

    def traverse(values, node=None, min=float("-inf"), max=float("inf")):
        nonlocal root
        if root is None:
            root = BST(values.pop())
            node = root
        if len(values) < 1:
            return
        if values[-1] >= min and values[-1] < node.value:  # going left
            node.left = BST(values.pop())
            traverse(values, node.left, min, node.value)
        if len(values) < 1:
            return
        if values[-1] < max and values[-1] >= node.value:  # going right
            node.right = BST(values.pop())
            traverse(values, node.right, node.value, max)
    traverse(values)
    return root


def traverse1(node):
    if node is None:
        return
    traverse1(node.left)
    print(node.value)
    traverse1(node.right)


res = reconstructBst([10, 4, 2, 1, 5, 17, 19, 18])
traverse1(res)
# print(validate.validateBst(res))
