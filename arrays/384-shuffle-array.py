import random


class Solution:

    def __init__(self, nums):
        self.deck = nums
        self.orig = nums.copy()

    def reset(self):
        self.deck = self.orig.copy()
        return self.orig

    def shuffle(self):
        # use fischer Yates algorithim
        end = len(self.deck) - 1
        while end > 0:
            idx = random.randint(0, end)  # actually an index to swap
            tmp = self.deck[idx]
            self.deck[idx] = self.deck[end]
            self.deck[end] = tmp
            end -= 1
        return self.deck


sol = Solution([1, 2, 3])
print(sol.shuffle())

# my guess

# def shuffle(self):
#     cards = {}
#     res = []
#     for num in self.deck:
#         cards[num] = 1 + cards.get(num, 0)
#     while len(cards.keys()):
#         keys = list(cards.keys())

#         rand = random.randint(0, len(cards.keys())-1)
#         res.append(keys[rand])
#         cards[keys[rand]] -= 1
#         if cards[keys[rand]] == 0:
#             del cards[keys[rand]]
#     return res
