class Solution:
    def nextGreaterElement(self, nums1, nums2):
        hash = {}
        stack = []
        res = []
        for el in nums2:
            while len(stack) and el > stack[-1]:
                p = stack.pop()
                hash[p] = el
            stack.append(el)
        for el in nums1:
            if el in hash:
                res.append(hash[el])
            else:
                res.append(-1)
        return res
