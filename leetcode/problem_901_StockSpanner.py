# class StockSpanner:

#     def __init__(self):
#         self.prices = []

#     def next(self, price: int) -> int:
#         self.prices.append(price)
#         if len(self.prices) == 1:
#             return 1
#         stack = self.prices[:-1]
#         curr_idx = len(self.prices) - 1

#         top_idx = curr_idx - 1
#         while stack and stack[-1] <= price:
#             top_idx = len(stack) - 2
#             stack.pop()
        
#         return curr_idx - top_idx


class StockSpanner:

    def __init__(self):
        self.stack = [] # pair: (price, span)

    def next(self, price: int) -> int:
        
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))

        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)