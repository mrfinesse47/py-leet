# 901. Online Stock Span

class StockSpanner:

    def __init__(self):
        self.prices = [[float("inf"), 0]]  # init to inf to avoid edge cases
        self.day = 0

    def next(self, price):
        while self.prices and self.prices[-1][0] <= price:
            self.prices.pop()
        self.day += 1
        self.prices.append([price, self.day])
        return self.day - self.prices[-2][1]

        # Explanation
stockSpanner = StockSpanner()
print(stockSpanner.next(5))  # return 1
print(stockSpanner.next(55))  # return 1
print(stockSpanner.next(60))  # return 1
print(stockSpanner.next(70))  # return 2
print(stockSpanner.next(60))  # return 1
# return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
print(stockSpanner.next(75))  # 4
print(stockSpanner.next(85))  # return 6
