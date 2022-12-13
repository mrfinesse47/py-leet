
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    def dfs(node, count=0, res=[]):
        count += node.value
        if node.left is None and node.right is None:
            res.append(count)
        if node.left:
            dfs(node.left, count, res)
        if node.right:
            dfs(node.right, count, res)
        return res
    return dfs(root)
