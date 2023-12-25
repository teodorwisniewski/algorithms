from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        total_profit = 0

        for idx in range(1, len(prices)):
            prev = prices[idx - 1]
            curr_price = prices[idx]
            diff = curr_price - prev
            if diff > 0:
                total_profit += diff

        return total_profit
            
        



prices = [7,1,5,3,6,4]

sol = Solution()
res = sol.maxProfit(prices)
print(f"maxProfit {res}")

assert 7 == res