def reverse(nums, l, r):
    while l < r:
        tmp = nums[r]
        nums[r] = nums[l]
        nums[l] = tmp
        l += 1
        r -= 1
    return nums


def rotate_array(nums, n):
    if n == 0:
        return nums
    l, r = 0, len(nums) - 1
    reverse(nums, l, r)

    r = len(nums) - 1
    l = n if n > 0 else len(nums)+n
    reverse(nums, l, r)
    r = n-1 if n > 0 else len(nums)-1+n
    l = 0
    reverse(nums, l, r)

    return nums


# nums = [1, 10, 20, 0, 59, 86, 32, 11, 9, 40]
# n = -2
print(rotate_array([1, 10, 20, 0, 59, 86, 32, 11, 9, 40], 3))


# [9, 40, 1, 10, 20, 0, 59, 86, 32, 11]
