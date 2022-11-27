# for lintcode and others

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


def genArrayOfIntervals(arr):
    res = []
    for el in arr:
        res.append(Interval(el[0], el[1]))
    return res


def printIntervalsFromArr(arr):
    count = 1
    res = []
    for el in arr:
        res.append([el.start, el.end])
    print(res)
