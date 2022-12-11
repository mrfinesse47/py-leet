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
        sum = 0
        max_sum = float("-inf")
        for el in lst:
            if sum < 0:  # can do this because 2 neg numbers added together is always
                # even more negative so the largest sum will only be a single negative number
                sum = 0
            sum += el
            r += 1
            max_sum = max(max_sum, sum)
        return max_sum


print(Solution().maxSubArray(lst))
