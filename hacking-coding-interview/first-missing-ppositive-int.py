def first_missing_positive(arr):

    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = 0
        if abs(arr[i]) <= len(arr):
            if arr[abs(arr[i])-1] > 0:
                arr[abs(arr[i])-1] *= -1
    print(arr)

    for i in range(len(arr)):
        if arr[i] == 0:
            return i + 1
    return 1


nums = [3, 4, -1, 1]  # 2
print(first_missing_positive(nums))
