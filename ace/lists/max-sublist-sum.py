def find_max_sum_sublist(lst):
    l, r = 0, 0
    sum = 0
    max_sum = float("-inf")
    while r < len(lst) and l <= r:
        while sum < 0:
            sum -= lst[l]
            l += 1
        sum += lst[r]
        r += 1
        max_sum = max(max_sum, sum)
    return max_sum


lst = [-4, 2, -5, 1, 2, 3, 6, -5]  # 1,2,3,6 ->12

# print(find_max_sum_sublist(lst))


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l, r = 0, 0
        sum = 0
        max_sum = float("-inf")
        while r < len(lst) and l <= r:
            while sum < 0:
                sum -= lst[l]
                l += 1
            sum += lst[r]
            r += 1
            max_sum = max(max_sum, sum)
        return max_sum


print(Solution().maxSubArray(lst))
