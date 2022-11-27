# 920 · Meeting Rooms -- lintcode

import generateIntervals as inter


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


# class Solution: brute force solution

#     def can_attend_meetings(self, intervals):
#         i = 0
#         while i < len(intervals):
#             j = i + 1
#             while j < len(intervals):
#                 if intervals[j].start > intervals[i].start and intervals[j].start < intervals[i].end:
#                     return False
#                 if intervals[j].end > intervals[i].start and intervals[j].start < intervals[i].end:
#                     return False
#                 j += 1
#             i += 1
#         return True


class Solution:

    def can_attend_meetings(self, intervals):
        i = 0
        intervals.sort(key=lambda x: x.start)
        while i < len(intervals)-1:
            if intervals[i].end > intervals[i+1].start:
                return False
            i += 1
        return True


my_int = inter.genArrayOfIntervals([[0, 30], [55, 100]])

print(Solution().can_attend_meetings(my_int))
