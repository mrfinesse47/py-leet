class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findNode(n1, n2, n3):
    found = False
    cur = n1
    while cur:
        if cur.value == n2.value:
            found = True
        if n3.value < cur.value:
            cur = cur.left
        elif n3.value > cur.value:
            cur = cur.right
        else:
            return True if found else False
    return False

# O(1) space O(h) time


def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    return findNode(nodeThree, nodeTwo, nodeOne) \
        or findNode(nodeOne, nodeTwo, nodeThree)
