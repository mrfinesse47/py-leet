import tree

# This is the class of the input root. Do not edit it.


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def flattenBinaryTree(root):
    def traverse(node, prev):
        if node is None:
            return prev
        traverse(node.left, node)
        print(node.value)
        if prev:
            prev.right = node
            #node.left = prev
        traverse(node.right, node)
        return prev

    prev = traverse(root, None)
    # print(prev.value)


bst = tree.BST(10).insert(5).insert(2).insert(7).insert(14)

flattenBinaryTree(bst)
