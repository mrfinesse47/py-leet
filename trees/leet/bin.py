class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insertNode(root, value):
    currentNode = root
    while True:

        if value < currentNode.val:
            if currentNode.left == None:
                currentNode.left = TreeNode(value)
                break
            else:
                currentNode = currentNode.left
        else:
            if currentNode.right == None:
                currentNode.right = TreeNode(value)
                break
            else:
                currentNode = currentNode.right
    return root


def traverse(root):
    print(root.val)
    if root == None:
        return
    if root.left:
        prev = root
        root = root.left
        traverse(root)
        root = prev
    if root.right:
        root = root.right
        traverse(root)
    return


root = TreeNode(10)
insertNode(root, 5)
insertNode(root, 2)
traverse(root)
