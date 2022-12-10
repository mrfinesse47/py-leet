def find_sum(lst, k):
    hash = {}
    for el in lst:
        if el in hash:
            return [hash[el], el]
        hash[k-el] = el
    return -1


lst = [1, 21, 3, 14, 5, 60, 7, 6]
k = 81

print(find_sum(lst, k))
