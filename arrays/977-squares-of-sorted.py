# 977. Squares of a Sorted Array


class Solution:
    def sortedSquares(self, arr):
        length = len(arr)
        l, r = 0, length-1
        res = [0]*length
        idx = length-1
        while idx >= 0:
            lsq = arr[l] * arr[l]
            rsq = arr[r] * arr[r]
            if lsq >= rsq:
                res[idx] = lsq
                l += 1
            else:
                res[idx] = rsq
                r -= 1
            idx -= 1
        return res


print(Solution().sortedSquares([-7]))
