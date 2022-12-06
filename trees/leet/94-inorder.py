# 94. Binary Tree Inorder Traversal

import bin as tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, node, res=None):
        res = [] if res is None else res
        org = node

        if node and node.left:
            node = node.left
            self.inorderTraversal(node, res)
        node = org
        if org:
            res.append(org.val)

        if node and node.right:
            node = node.right
            self.inorderTraversal(node, res)
        return res


root = TreeNode(10)
tree.insertNode(root, 5)
tree.insertNode(root, 2)

print(Solution().inorderTraversal(root))
print(Solution().inorderTraversal(None))
