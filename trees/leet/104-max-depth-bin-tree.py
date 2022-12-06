import bin as tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root):
        if root == None:
            return 0

        if root.left == None and root.right == None:
            return 1

        def dfs(node, count):
            if node is None:
                return
            if node.left:
                count += 1
                max_count[0] = max(count, max_count[0])
                dfs(node.left, count)
                count -= 1
            if node.right:
                count += 1
                max_count[0] = max(count, max_count[0])
                dfs(node.right, count)
                count -= 1
            return max

        count = 1
        max_count = [0]

        dfs(root, count)
        return max_count[0]


root = TreeNode(3)
tree.insertNode(root, 9)
tree.insertNode(root, 20)
tree.insertNode(root, 15)
tree.insertNode(root, 7)
# tree.insertNode(root, 6)
# tree.insertNode(root, 9)
# tree.traverse(root)

print(Solution().maxDepth(root))
