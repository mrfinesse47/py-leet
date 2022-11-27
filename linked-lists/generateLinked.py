# linked list generation to test put leetcode solutions

# the leetcode defintion of a linked list node

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


def generateFromList(list):
    head = ListNode()
    node = head
    for el in list:
        node.next = ListNode(el)
        node = node.next
    return head.next

# generate
# takes an array or num, array -> linked list, num generaes number of nodes in increasing value


def generate(num):
    if type(num) == list:
        return generateFromList(num)
    counter = 1
    head = ListNode(counter)
    node = head
    counter += 1
    while counter <= num:
        node.next = ListNode(counter)
        node = node.next
        counter += 1
    return head

# prints out a linked list from a particular node to end


def printLinkedList(node):
    res = []
    while node:
        res.append(node.data)
        node = node.next
    print(res)
