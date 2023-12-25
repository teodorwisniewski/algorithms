from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        # mapping part
        for n in nums:
            idx = abs(n) - 1
            nums[idx] = -1 * abs(nums[idx])
        
        # find missing numbers
        res = []
        for idx, n in enumerate(nums):
            if n > 0:
                res.append(idx+1)
        return res
    

sol = Solution()

nums = [4, 3, 2, 7, 8, 2, 3, 1]
res = sol.findDisappearedNumbers(nums)
print(f"findDisappearedNumbers {res}")