def min_sub_array_len(target, arr):
    l, r = 0, 0
    sum = 0
    min_len = float("inf")

    while r < len(arr):
        sum += arr[r]

        while sum >= target:
            min_len = min(min_len, r-l+1)
            sum -= arr[l]
            l += 1
        r += 1

    return 0 if min_len == float("inf") else min_len


arr = [2, 2, 2, 2, 2]

print(min_sub_array_len(7, arr))
