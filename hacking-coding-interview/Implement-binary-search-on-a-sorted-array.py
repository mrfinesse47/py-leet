def recursive_binary_search(nums, target, l=0, r=None):
    if r == None:
        r = len(nums) - 1
    if l > r:
        return -1
    m_idx = l + (r-l)//2
    mid = nums[m_idx]
    if mid == target:
        return m_idx
    elif mid > target:
        return recursive_binary_search(nums, target, l, m_idx-1)
    else:
        return recursive_binary_search(nums, target,  m_idx+1, r)


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
    # is the same as l < r due to exit of while for return -1
    return -1


nums = []
target = 100

print(binary_search([-1, 0, 3, 5, 9, 12], 0))
