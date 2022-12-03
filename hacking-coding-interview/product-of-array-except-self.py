def product_except_self(nums):
    length = len(nums)
    if length <= 1:
        return nums
    pre = nums.copy()
    post = nums.copy()
    answer = []
    for i in range(1, length):
        pre[i] *= pre[i-1]
        post[i*-1 - 1] *= post[i*-1]
    for i in range(length):
        if i == 0:
            answer.append(post[i+1])
        elif i == length-1:
            answer.append(pre[i-1])
        else:
            answer.append(pre[i-1]*post[i+1])
    return answer


nums = [1, 2, 3]

print(product_except_self(nums))
