
def minHeightBst(arr, root=None):
    if len(arr) == 1:
        return BST(arr[0]) if root == None else root.insert(arr[0])
    half = len(arr)//2
    if root == None:
        root = BST(arr[half])
    else:
        root.insert(arr[half])
    l = arr[0:half]
    minHeightBst(l, root)
    r = arr[half+1:len(arr)]
    if r:
        minHeightBst(r, root)
    return root


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

    def traverse(self):
        print(self.value)
        if self == None:
            return
        if self.left:
            prev = self
            self = self.left
            self.traverse()
            self = prev
        if self.right:
            self = self.right
            self.traverse()
        return


array = [1, 2, 5, 7, 10, 13, 14, 15, 22]

bst = minHeightBst(array)
bst.traverse()
