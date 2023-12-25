from typing import List
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        for i, val in enumerate(nums):
            nums[i] = str(val)

        def custom_compare(x, y):
            if x+y > y+x:
                return -1
            else:
                return 1
        
        nums = sorted(nums, key=cmp_to_key(custom_compare))
        return str(int("".join(nums)))





sol = Solution()
nums = [3, 30, 34, 5, 9]
res = sol.largestNumber(nums)
print(f"largestNumber {res}")