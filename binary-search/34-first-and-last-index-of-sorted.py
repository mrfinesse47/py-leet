# 34. Find First and Last Position of Element in Sorted Array

class Solution:
    def binarySearch(self, arr, target, res):
        l, r = 0, len(arr)-1
        while l <= r:
            m = l + (r-l)//2
            if arr[m] == target:
                if res[0] == -1:
                    if m == 0 or arr[m] != arr[m-1]:
                        res[0] = m
                        return res
                    else:
                        r = m-1
                else:
                    if m == len(arr)-1 or arr[m] != arr[m+1]:
                        res[1] = m
                        return res
                    else:
                        l = m+1
            elif arr[m] < target:
                l = m+1
            else:
                r = m-1
        return res

    def searchRange(self, arr, target):
        res = [-1, -1]
        self.binarySearch(arr, target, res)
        if res[0] != -1:
            self.binarySearch(arr, target, res)

        return res


nums = []
target = 1

print(Solution().searchRange(nums, target))
