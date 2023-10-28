from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0

        for idx in range(1, len(prices)):

            if prices[idx] > prices[idx-1]:
                profit += prices[idx] - prices[idx-1]
        return profit


prices = [7,1,5,3,6,4]

sol = Solution()
res = sol.maxProfit(prices)
print(f"maxProfit {res}")

assert 7 == res