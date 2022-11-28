# 739. Daily Temperatures
# monotonic stack

# [73,74,75,71,73,72,76,74]

# [x,x,75,71]
# [x,x,75,x,73]


class Solution:
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures)
        stack = []  # [temp,index]
        None
