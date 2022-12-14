# 543. Diameter of Binary Tree

import bin as tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        maxD = 0

        def max_depth(root):
            nonlocal maxD
            if not root:
                return 0
            left = 0
            right = 0
            if root.left:
                left = 1+max_depth(root.left)
            if root.right:
                right = 1+max_depth(root.right)
            maxD = max(maxD, right+left)
            return max(left, right)
        max_depth(root)
        return maxD


root = TreeNode(6)
tree.insertNode(root, 4)
tree.insertNode(root, 2)
tree.insertNode(root, 5)
tree.insertNode(root, 7)


print(Solution().diameterOfBinaryTree(root))
