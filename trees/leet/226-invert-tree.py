
import bin as tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root):
        def helper(root):
            if not root:
                return
            tmp = root.left
            root.left = root.right
            root.right = tmp
            self.invertTree(root.left)
            self.invertTree(root.right)
        orig = root
        helper(root)
        return orig


root = TreeNode(4)
tree.insertNode(root, 2)
tree.insertNode(root, 7)
tree.insertNode(root, 1)
tree.insertNode(root, 3)
tree.insertNode(root, 6)
tree.insertNode(root, 9)
tree.traverse(root)
print("########")
print(Solution().invertTree(None))
