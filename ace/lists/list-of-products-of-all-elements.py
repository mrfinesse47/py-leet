def find_product(lst):
    prod = 1
    lst2 = []
    for i in range(len(lst)):
        lst2.append(prod)
        prod *= lst[i]
    right = 1
    for i in range(len(lst)-1, -1, -1):
        lst2[i] = lst2[i]*right
        right = lst[i] * right
    return lst2


arr = [1, 2, 3, 4]

print(find_product(arr))
