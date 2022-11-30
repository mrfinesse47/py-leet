class Interval:
    def __init__(self, first, second):
        self.first = first
        self.second = second


def merge_intervals(v):
    if not v:
        return None
    if len(v) == 1:
        return v
    result = []
    result.append(v[0])
    for i in range(1, len(v)):
        if v[i].first <= result[-1].second:
            result[-1].second = max(v[i].second, result[-1].second)
            # must remember to always take the greater of the second not just
            # set it to the second etc.
        else:
            result.append(v[i])
    return result


def create_intervals(v):
    res = []
    for el in v:
        res.append(Interval(el[0], el[1]))
    return res


def print_intervals(v):
    for inter in v:
        print(inter.first, inter.second)


intervals = create_intervals([[1, 3], [2, 6], [8, 10], [15, 18]])

print_intervals(merge_intervals(intervals))
