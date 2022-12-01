arr = [2, 1, 8, 4, 7, 3]
val = 2


def find_sum_of_two(arr, val):
    hash = {}
    for el in arr:
        if el in hash:
            return True
        hash[val - el] = el

    return False


print(find_sum_of_two(arr, 2))
