import tree


def findKthLargestValueInBst(tree, k):
    count = 0
    res = -1

    def traverse(node, k):
        if node is None:
            return
        nonlocal count, res
        traverse(node.right, k)
        count += 1
        if count == k:
            res = node.value
            return
        traverse(node.left, k)

    traverse(tree, k)
    return res


bst = tree.BST(15).insert(5).insert(5).insert(
    2).insert(1).insert(3).insert(20).insert(17).insert(22)

print(findKthLargestValueInBst(bst, 9))
