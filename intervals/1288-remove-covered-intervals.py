# 1288. Remove Covered Intervals

class Solution:
    def removeCoveredIntervals(self, arr):
        arr.sort(key=lambda x: (x[0], x[1]))
        res = []
        res.append(arr[0])
        for el in arr[1:len(arr)]:
            lastRes = res[len(res)-1]
            if lastRes[0] == el[0]:
                lastRes[1] = el[1]
            elif not lastRes[1] >= el[1]:
                res.append(el)
        return len(res)


arr = [[1, 2], [1, 4], [3, 4]]  # 3,6 covered by 2,8 therefore noi 3,6

print(Solution().removeCoveredIntervals(arr))
