# 56. Merge Intervals

class Solution:
    def merge(self, arr):
        res = []
        arr.sort(key=lambda x: x[0])
        res.append(arr[0])
        for el in arr[1:len(arr)]:
            resLast = len(res) - 1
            if el[0] <= res[resLast][1]:
                res[resLast][1] = max(el[1], res[resLast][1])
            else:
                res.append(el)
        return res
