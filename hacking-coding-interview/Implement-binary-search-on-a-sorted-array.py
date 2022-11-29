

def binary_search(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        guessIdx = l + (r-l)//2
        guessNum = nums[guessIdx]
        if guessNum == target:
            return guessIdx
        elif guessNum > target:
            r = guessIdx - 1
        else:
            l = guessIdx + 1
    return -1


nums = []
target = 100

print(binary_search([-1, 0, 3, 5, 9, 12], 9))
