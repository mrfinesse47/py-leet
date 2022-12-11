class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def traverse(self):

        if self == None:
            return
        self.traverse(self.left)
        print(self.value)
        self.traverse(self.left)
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

    def getSuccessor(self, node):
        # also severs the parents left or right to this node
        if node.right:
            prev = node
            node = node.right
        if node.left == None:
            prev.right = None
            return node
        while node and node.left:
            prev = node
            node = node.left
        prev.left = None
        return node

    def getNode(self, value):
        node = self
        while node:
            if node.value == value:
                return node
            elif value < node.value:
                node = node.left
            else:
                node = node.right
        return None

    def remove(self, value):
        if self.left == None and self.right == None:
            self = None
            return self
        currentNode = self
        prevLeft = None  # set the other to none if last was right etc
        prevRight = None

        while currentNode:

            if value == currentNode.value:
                break
            elif value < currentNode.value:
                prevLeft = currentNode
                prevRight = None
                currentNode = currentNode.left
            elif value > currentNode.value:
                prevRight = currentNode
                prevLeft = None
                currentNode = currentNode.right

        if currentNode == None:
            return self  # node wasnt found

        if currentNode.left and currentNode.right:
            successor = self.getSuccessor(currentNode)
            successor.left = currentNode.left
            successor.right = currentNode.right
            if prevLeft:
                prevLeft.left = successor
            elif prevRight:
                prevRight.right = successor
            else:  # removing root
                self.value = successor.value
                self.left = successor.left
                self.right = successor.right
        elif currentNode.left:  # single child left
            if prevLeft:
                prevLeft.left = currentNode.left
            elif prevRight:
                prevRight.right = currentNode.left
            else:
                currentNode = currentNode.left
                self.value = currentNode.value
                self.left = currentNode.left
                self.right = currentNode.right
        elif currentNode.right:  # single child right
            if prevLeft:
                prevLeft.left = currentNode.right
            elif prevRight:
                prevRight.right = currentNode.right
            else:
                currentNode = currentNode.right
                self.value = currentNode.value
                self.left = currentNode.left
                self.right = currentNode.right
        else:  # no children
            if prevLeft:
                prevLeft.left = None
            elif prevRight:
                prevRight.right = None

        return self


# tree = BST(1).insert(2).insert(3).insert(4)

# tree = tree.remove(1)

# if tree:
#     print("traverse")
#     tree.traverse()
#print("successor of:", node.value, " is:", tree.getSuccessor(node).value)
