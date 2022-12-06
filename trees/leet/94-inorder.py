# 94. Binary Tree Inorder Traversal

import bin as tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root):
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        res = []
        inorder(root)
        return res

    def inorderTraversal(self, root):
        if root == None:
            return []
        cur = root
        stack, res = [], []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right

        return res


root = TreeNode(10)
tree.insertNode(root, 5)
tree.insertNode(root, 7)
tree.insertNode(root, 2)
tree.insertNode(root, 14)

print(Solution().inorderTraversal(root))
# print(Solution().inorderTraversal(None))
