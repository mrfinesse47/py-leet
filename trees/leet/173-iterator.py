# 173. Binary Search Tree Iterator
import bin as tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root):
        self.stk = []
        self.populate_iterator(root)

    def populate_iterator(self, root):
        while root:
            self.stk.append(root)
            root = root.left

    def hasNext(self):
        if not self.stk:
            return False
        else:
            return True

    def next(self):
        if not self.stk:
            return None

        r_val = self.stk[-1]
        del self.stk[-1]
        temp = r_val.right
        self.populate_iterator(temp)
        return r_val.val


root = TreeNode(7)
tree.insertNode(root, 3)
tree.insertNode(root, 15)
tree.insertNode(root, 9)
tree.insertNode(root, 20)

iter = BSTIterator(root)
iter.next()
iter.next()
iter.next()
iter.next()
print(iter.hasNext())
iter.next()
print(iter.hasNext())
