from typing import List




class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_sub = self.find_max_val(nums)
        current_sum = 0
        for num in nums:
            if current_sum + num < 0:
                current_sum = 0
            else:
                current_sum += num
                if current_sum > max_sub:
                    max_sub = current_sum    

        return max_sub
    
    def find_max_val(self, nums):

        max_val = float("-inf")
        for num in nums:
            if num > max_val:
                max_val = num
        return max_val



nums = [-2,1,-3,4,-1,2,1,-5,4]

sol = Solution()
res = sol.maxSubArray(nums)
print(f"maxSubArray {res}")

res2 = sol.maxSubArray([-1])
print(f"maxSubArray {res2}")