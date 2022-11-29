# 33. Search in Rotated Sorted Array
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = l + (r-l)//2
            if nums[m] == target:
                return m
            elif nums[l] <= nums[m]:  # lhs is sorted
                # between the sorted left side
                if target <= nums[m] and target >= nums[l]:
                    r = m-1
                else:
                    l = m+1  # between the unsorted right side
            else:  # rhs is sorted
                if target >= nums[m] and target <= nums[r]:
                    l = m+1  # between the sorted right side
                else:
                    r = m-1  # between the unsorted left side
        return -1


# if searching for 0
# we look at 2 halves
# 4-6
# and 7-2
# we know 0 cannot exist between 4-6 but somehow is within 7-2
# find the sorted half
# so we take 7-2 side
# then we have 7-0 and 1-2, it cant exist between 1-2
nums = [4, 5, 6, 7, 0, 1, 2]
target = 7

print(Solution().search(nums, target))
