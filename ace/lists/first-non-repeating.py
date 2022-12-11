def find_first_unique(lst):
    sHash = {}
    for el in lst:
        sHash[el] = 1 + sHash.get(el, 0)
    for el in lst:
        if sHash[el] < 2:
            return el


print(find_first_unique([9, 2, 3, 2, 6, 6, 9]))
