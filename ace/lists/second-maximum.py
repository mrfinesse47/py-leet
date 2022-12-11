# def find_second_maximum(lst):  # n space
#     stack = [float("-inf"), float("-inf")]
#     for el in lst:
#         if el > stack[-1]:
#             stack.append(el)
#         else:
#             if el > stack[-2]:
#                 stack[-2] = el
#     if stack[-2] != float("-inf"):
#         return stack[-2]

def find_second_maximum(lst):  # O(1) Space O(n) time
    biggest, bigger = float("-inf"), float("-inf")
    for el in lst:
        if el > biggest:
            bigger = biggest
            biggest = el
        elif el > bigger:
            bigger = el
    return bigger


lst = [10, 2, 3, 6, 7, 9]

print(find_second_maximum(lst))
