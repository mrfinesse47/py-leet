# 456. 132 Pattern


class Solution:
    def find132pattern(self, nums):
        maxs = []
        min = float("inf")
        for num in nums:
            min = min(min, num)
            if maxs.length < 1:
                maxs.append(num)
            else:
                while maxs and num > maxs[-1]:
                    maxs.pop()
                else:
                    maxs.append(num)

        return False


print(Solution().find132pattern([3, 1, 3, 2]))

# [3,1,4,0,2]
# [1,3,4]

#  [1,3,6,8,7,4]
# [1,3]
# -1,3,2
