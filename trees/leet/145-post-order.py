# 145. Binary Tree Postorder Traversal

import bin as tree


class Solution:
    def postorderTraversal(self, root):
        pass


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(20)
tree.insertNode(root, 9)
tree.insertNode(root, 21)
tree.insertNode(root, 22)
tree.insertNode(root, 7)
