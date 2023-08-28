from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        greatest_profit = 0
        current_buy = prices[0]

        for price in prices:

            potential_profit = price - current_buy

            if price < current_buy:
                current_buy = price
            elif potential_profit > greatest_profit:
                greatest_profit = potential_profit

        return greatest_profit



prices = [7,1,5,3,6,4]

sol = Solution()
res = sol.maxProfit(prices)
print(f"maxProfit {res}")

assert 5 == res