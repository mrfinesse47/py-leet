class Solution:
    def removeDuplicates(self, str, k):
        stack = []  # [char,count]
        res = ""
        for char in str:
            if len(stack) and char == stack[-1][0]:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])

        for el in stack:
            res += el[0] * el[1]

        return res


print(Solution().removeDuplicates("ddd", 2))
