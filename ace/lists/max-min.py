def max_min(lst):
    result = []
    # iterate half list
    for i in range(len(lst)//2):
        result.append(lst[-(i+1)])
        # append current element
        result.append(lst[i])
    if len(lst) % 2 == 1:
        # if middle value then append
        result.append(lst[len(lst)//2])
    return result


lst = [1, 2, 3, 4, 5]
# [5,1,4,2,3]
print(max_min(lst))
