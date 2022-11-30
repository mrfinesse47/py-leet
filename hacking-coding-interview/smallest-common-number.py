# Find the Smallest Common Number

def find_least_common_number(arr1, arr2, arr3):
    arr1.reverse()  # oops reversing is o(n), could have used iterators
    arr2.reverse()
    arr3.reverse()
    while arr1 and arr2 and arr3:
        if arr1[-1] == arr2[-1] and arr2[-1] == arr3[-1]:
            return arr1[-1]
        elif arr1[-1] <= arr2[-1] and arr1[-1] <= arr3[-1]:
            arr1.pop()
        elif arr2[-1] <= arr1[-1] and arr2[-1] <= arr3[-1]:
            arr2.pop()
        else:
            arr3.pop()

    return -1


v1 = [6, 7, 10, 25, 30, 50, 63, 64]
v2 = [0, 4, 5, 6, 7, 8]
v3 = [1, 2, 8, 10, 14, 50]

print(find_least_common_number(v1, v2, v3))
