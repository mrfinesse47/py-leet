import tree


def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array


def preOrderTraverse(tree, array):
    if tree is not None:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
    return array


def postOrderTraverse(tree, array):
    if tree is not None:

        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)
    return array


bst = tree.BST(10).insert(5).insert(15).insert(
    2).insert(5).insert(1).insert(22)

print(inOrderTraverse(bst, []))
print(preOrderTraverse(bst, []))
print(postOrderTraverse(bst, []))
