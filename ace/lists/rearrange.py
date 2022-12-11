def rearrange(lst):
    l, r = 0, len(lst)-1
    while l < r:
        while lst[l] < 0:
            l += 1
        while lst[r] >= 0:
            r -= 1
        if l < r:
            tmp = lst[l]
            lst[l] = lst[r]
            lst[r] = tmp
        l += 1
        r -= 1
    return lst


lst = [10, -1, 20, 4, 5, -9, -6]
# [-1,-9,-6,10,20,4,5]
print(rearrange(lst))
