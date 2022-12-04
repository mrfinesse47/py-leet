class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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

    def insert(self, value):
        currentNode = self
        while True:

            if value < currentNode.value:
                if currentNode.left == None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right == None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self

    # runs worst case O(N) time avg O(log(N))

    def contains(self, value):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True
        return False

    def remove(self, value):
        currentNode = self
        prevLeft = None  # set the other to none if last was right etc
        prevRight = None
        # if node is root, both prev will be none set new root
        # find previous node to set its next
        # if no children just set prev ptr to None
        # if only one child set prev to the child of the removed node
        # if 2 children find next greatest ancestor
        # set the prev for that ancestor to prev of node removed
        # set prev for the removed node to the ancestor, set left of ancestor to the old nodes left
        while currentNode and currentNode.value != value:
            pass

        return self


node = BST(10).insert(5).insert(2).insert(5).insert(1).insert(
    15).insert(13).insert(12).insert(14).insert(22)

node.traverse()
