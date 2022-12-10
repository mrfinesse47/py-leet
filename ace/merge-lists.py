def merge_lists(lst1, lst2):
    res = []
    i, k = 0, 0
    while i < len(lst1) and k < len(lst2):
        if lst1[i] <= lst2[k]:
            res.append(lst1[i])
            i += 1
        else:
            res.append(lst2[k])
            k += 1

    if i < len(lst1):
        res.extend(lst1[i:])  # [i:] same as [i:len(lst1)]
    elif k < len(lst2):
        res.extend(lst2[k:])
    return res


list1 = [1, 3, 4, 5]
list2 = [2, 6, 7, 8]

print(merge_lists(list1, list2))
