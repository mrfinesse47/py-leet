# 2149. Rearrange Array Elements by Sign
class Solution:
    def rearrangeArray(self, nums):
        res = [0]*len(nums)
        negi, posi = 1, 0
        for i in range(len(nums)):
            if nums[i] > 0:
                res[posi] = nums[i]
                posi += 2
            else:
                res[negi] = nums[i]
                negi += 2
        return res


nums = [3, 1, -2, -5, 2, -4]  # [3,-2,1,-5,2,-4]
print(Solution().rearrangeArray(nums))
