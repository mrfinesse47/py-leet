def reverse_part(lst, i, j):
    while i < j:
        tmp = lst[i]
        lst[i] = lst[j]
        lst[j] = tmp
        i += 1
        j -= 1


def right_rotate(lst, k):
    if len(lst) == 0:
        return lst
    k %= len(lst)
    reverse_part(lst, 0, len(lst)-1)
    reverse_part(lst, 0, k-1)
    reverse_part(lst, k, len(lst)-1)
    return lst


lst = [10, 20, 30, 40, 50]
# [50,40,30,20,10]
# reverse halves at 0->2 and 3->4
# [30,40,50,10,20]

k = 3

print(right_rotate(lst, 0))


def right_rotate_pythonic(lst, k):
    # get rotation index
    if len(lst) == 0:
        k = 0
    else:
        k = k % len(lst)
    return lst[-k:] + lst[:-k]


test = "abcdefghi"

print(test[-5:])  # start at 5 from end to end ie index 4
print(test[:-5])  # up to and not inluding 5 from end or index 4
