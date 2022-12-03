def largestRange(array):
    mset = set()
    maxres = [array[0]]*2
    res = [array[0]]*2
    for el in array:
        mset.add(el)
    for el in array:
        low, high = -1, 1
        res = [el, el]
        while el + low in mset:
            mset.remove(el + low)
            res[0] = el+low
            low -= 1
        while el + high in mset:
            mset.remove(el + high)
            res[1] = el+high
            high += 1
        if res[1]-res[0] > maxres[1]-maxres[0]:
            maxres = res
    return maxres


arr = [1]

print(largestRange(arr))
