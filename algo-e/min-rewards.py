def minRewards(scores):
    length = len(scores)
    candy = [1]*length

    for i in range(length-1):
        if scores[i+1] > scores[i]:
            candy[i+1] = max(candy[i+1], candy[i]+1)
    for i in range(length-1, 0, -1):
        if scores[i-1] > scores[i]:
            candy[i-1] = max(candy[i-1], candy[i]+1)

    return sum(candy)


scores = [2, 20, 13, 12, 11, 8, 4, 3, 1, 5, 6, 7, 9, 0]

print(minRewards(scores))
