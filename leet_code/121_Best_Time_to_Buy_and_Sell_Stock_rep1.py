from typing import List


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:

#         left, right = 0, 1
#         max_profit = 0
        
#         while right < len(prices):
#             if prices[left] < prices[right]:
#                 profit = prices[right] - prices[left]
#                 max_profit = max(profit, max_profit)
#             else:
#                 left = right

#             right += 1
    
#         return max_profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        current_buy = prices[0]
        
        for price in prices[1:]:
            potential_profit = price - current_buy
            if current_buy > price:
                current_buy = price
            elif potential_profit > max_profit:
                max_profit = potential_profit
            
        return max_profit



prices = [7,1,5,3,6,4]

sol = Solution()
res = sol.maxProfit(prices)
print(f"maxProfit {res}")

assert 5 == res