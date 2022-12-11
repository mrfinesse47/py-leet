import validate


class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def traverse(self):
        print(self.value)
        if self == None:
            return
        if self.left:
            prev = self
            self = self.left
            self.traverse()
            self = prev
        if self.right:
            self = self.right
            self.traverse()
        return


def reconstructBst(values):
    values.reverse()  # mistake made forgot to reverse for easy pop
    root = None

    def traverse(values, node, min=float("-inf"), max=float("inf")):
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
    traverse(values, root)
    return root


res = reconstructBst([10, 17, 19, 18, 4, 5, 2, 1])
print(validate.validateBst(res))
