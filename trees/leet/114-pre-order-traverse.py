# 144. Binary Tree Preorder Traversal

import bin as tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root, res=None):
        if res is None:
            res = []
        if root is None:
            return res
        res.append(root.val)
        self.preorderTraversal(root.left, res)
        self.preorderTraversal(root.right, res)
        return res

    def preorderTraversal(self, node):
        res, stack = [], []
        while node or stack:
            while node:
                stack.append(node)
                res.append(node.val)
                node = node.left
            node = stack.pop()
            node = node.right
        return res


root = TreeNode(20)
tree.insertNode(root, 9)
tree.insertNode(root, 21)
tree.insertNode(root, 22)
tree.insertNode(root, 7)

print(Solution().preorderTraversal(root))
