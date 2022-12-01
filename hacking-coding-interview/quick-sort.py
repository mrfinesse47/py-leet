def quicksort(arr, l=0, r=None):
    if r-l < 1:
        return
    lowerCount = 0 + l  # the biggest trick is to remember you are operating on the entire array so you need to offset the under count by l
    # maybe lower count is a bad name for it, it is more like a piviot index between l and r
    for i in range(l, r+1):
        if arr[i] < arr[l]:
            lowerCount += 1
            tmp = arr[i]
            arr[i] = arr[lowerCount]
            arr[lowerCount] = tmp
    tmp = arr[lowerCount]
    arr[lowerCount] = arr[l]
    # you have to be careful to offset lowercount in realtion to l
    arr[l] = tmp
    quicksort(arr, l, lowerCount - 1)
    quicksort(arr, lowerCount+1, r)


def quick_sort(arr):
    quicksort(arr, 0, len(arr)-1)
    return arr


arr = [49, 5]
print(quick_sort(arr))
