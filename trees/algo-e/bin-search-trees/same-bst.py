def sameBsts(arrayOne, arrayTwo, start=True):
    if start == True:
        arrayOne.reverse()
        arrayTwo.reverse()
        start = False
    if len(arrayOne) != len(arrayTwo):
        return False
    if len(arrayOne) < 1 or len(arrayTwo) < 1:
        return True
    el1 = arrayOne.pop()
    el2 = arrayTwo.pop()
    if el1 != el2:
        return False
    ar1 = [e for e in arrayOne if e >= el1]
    ar1 = [e for e in arrayTwo if e >= el1]
    res = sameBsts(ar1, ar2, start)
    if res == False:
        return False
    ar1 = list(filter(lambda a: a < el1, arrayOne))
    ar2 = list(filter(lambda a: a < el2, arrayTwo))
    return sameBsts(ar1, ar2, start)


arr1 = [10, 8, 5, 15, 2, 12, 11, 94, 81]
arr2 = [10, 15, 8, 12, 94, 81, 5, 2, 11]

print(sameBsts(arr1, arr2))

# more than 10 both arr : [15,12,11,94,81]
#                         [15,12,94,81,11]
# LESS thank 10  ``      :
# [8,5,2]
# [8,5,2]

# greater than 15:  94,81
#                   94,81

# less than 15: 12,11
# .             12,11
