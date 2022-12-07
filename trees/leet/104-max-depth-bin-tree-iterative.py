import bin as tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                # just like a function call basically
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res


root = TreeNode(3)

tree.insertNode(root, 5)
tree.insertNode(root, 2)
tree.insertNode(root, 3)
tree.insertNode(root, 1)
tree.insertNode(root, 4)
tree.insertNode(root, 6)
# tree.traverse(root)
# print(root.right.val)

print(Solution().maxDepth(root))
