# 1838. Frequency of the Most Frequent Element

# The frequency of an element is the number of times it occurs in an array.
# You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.
# Return the maximum possible frequency of an element after performing at most k operations.

class Solution:
    def maxFrequency(self, arr, k):
        l, r = 0, 0
        maxEl = 1
        arr.sort(reverse=True)
        count = 0
        while r < len(arr):
            count += arr[l] - arr[r]
            while count > k:
                prev = arr[l]
                l += 1
                count -= (prev-arr[l]) * (r-l+1)
            maxEl = max(maxEl, (r-l+1))
            r += 1
        return maxEl


arr = [1, 2, 6, 3]

print(Solution().maxFrequency(arr, 11))
