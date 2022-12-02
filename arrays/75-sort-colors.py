# 75. Sort Colors

def sortColors(self, arr):
    l, c, r = 0, 0, len(arr)-1
    while c <= r:
        tmp = arr[c]
        if arr[c] == 0:
            arr[c] = arr[l]
            arr[l] = tmp
            c += 1
            l += 1
        elif arr[c] == 1:
            c += 1
        else:
            arr[c] = arr[r]
            arr[r] = tmp
            r -= 1
    return arr
