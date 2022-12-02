import functools


class Solution:
    def largestNumber(self, nums):
        nums = list(map(lambda n: str(n), nums))

        def sortfx(s1, s2):
            if int(s1+s2) > int(s2+s1):
                return -1  # reverse order on -1 so the lower comes second
            elif int(s1+s2) < int(s2+s1):
                return 1  # normal order on 1
            else:
                return 0

        nums.sort(key=functools.cmp_to_key(sortfx))
        nums = "".join(nums)
        return "0" if int(nums) == 0 else nums


nums = [3, 30, 34, 5, 9]
print(Solution().largestNumber(nums))
