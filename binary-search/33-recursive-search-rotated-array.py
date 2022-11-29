class Solution:
    def recursive(self, nums, target, l, r):
        if (l > r):
            return -1
        m = l + (r-l)//2
        if nums[m] == target:
            return m
        elif nums[l] <= nums[m]:
            if target <= nums[m] and target >= nums[l]:
                r = m-1
            else:
                l = m+1
        else:
            if target >= nums[m] and target <= nums[r]:
                l = m+1
            else:
                r = m-1
        return self.recursive(nums, target, l, r)

    def search(self, nums, target):
        return self.recursive(nums, target, 0, len(nums)-1)


nums = [4, 5, 6, 7, 0, 1, 2]
target = 3

print(Solution().search(nums, target))
