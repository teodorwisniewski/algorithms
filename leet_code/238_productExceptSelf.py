
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1 for _ in range(n)]

        prefix = 1
        for i, num in enumerate(nums):
            res[i] *= prefix
            prefix *= num
        
        postfix = 1
        for i in range(n-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
        





sol = Solution()


nums = [1,2,3,4]
res = sol.productExceptSelf(nums)

print(f"productExceptSelf {res}")
