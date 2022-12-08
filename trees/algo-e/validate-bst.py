import tree


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    # Write your code here.
    def dfs(node):
        if node is None:
            return
        print(node.value)
        dfs(node.left)
        dfs(node.right)
    dfs(tree)


bst = tree.BST(10).insert(5).insert(5).insert(
    2).insert(1).insert(15).insert(13).insert(14).insert(22)

validateBst(bst)
# bst.traverse()
