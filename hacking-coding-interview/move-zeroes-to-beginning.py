# Move All Zeros to the Beginning of the Array

def move_zeros_to_left(nums):
    zeroCount = 0
    for i in range(len(nums)-1, -1, -1):
        if nums[i] == 0:
            zeroCount += 1
        else:
            nums[i+zeroCount] = nums[i]
    for i in range(0, zeroCount):
        nums[i] = 0
    return nums


nums = [1, 0, 0, 0, 0, 0, 0]

move_zeros_to_left(nums)

print(nums)
