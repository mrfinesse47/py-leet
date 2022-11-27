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
    for el in arr:
        print("interval:", count, ", start:", el.start, " end:", el.end)
        count += 1
