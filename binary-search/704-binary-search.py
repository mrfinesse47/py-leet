# 704. Binary Search

class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums)-1

        while l <= r:
            # the r-l becomes 0 so the pointers meet making m the left pointer in the
            m = l + (r-l)//2
            # last go around before the l<=r condition is exceeded
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 12

print(Solution().search(nums, target))
