


from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negatives_cnt = 0
        for num in nums:
            if not num:
                return 0
            if num < 0:
                negatives_cnt += 1
        
        if (negatives_cnt % 2) == 0:
            return 1
        else:
            return -1
      
        


sol = Solution()
nums = [-1,-2,-3,-4,3,2,1]
res = sol.arraySign(nums)
assert res == 1



nums = [1,5,0,2,-3]
res = sol.arraySign(nums)
assert res == 0


nums = [-1,1,-1,1,-1]
res = sol.arraySign(nums)
assert res == -1