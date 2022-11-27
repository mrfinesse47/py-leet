# from grokking

# Problem Statement

# Given a list of intervals, merge all the overlapping intervals to produce
# a list that has only mutually exclusive intervals.
import generateIntervals as inter


class Solution:
    def merge(self, arr):
        res = []
        arr.sort(key=lambda x: x[0])
        for el in arr:
            if len(res) == 0:
                res.append(el)
            else:
                resLast = len(res) - 1
                if el[0] <= res[resLast][1]:
                    res[resLast][1] = max(el[1], res[resLast][1])
                else:
                    res.append(el)
        return res


my_int = inter.genArrayOfIntervals([])

inter.printIntervalsFromArr(Solution().merge(my_int))
