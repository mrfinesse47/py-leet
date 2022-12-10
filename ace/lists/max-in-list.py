def find_minimum(arr):
    mixm = float("inf")
    for el in arr:
        mixm = min(el, mixm)
    return mixm


print(find_minimum([9, 2, 3, 6]))
