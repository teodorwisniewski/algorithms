from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        conseq_zeros = 0
        for num in nums:
            if not num:
                conseq_zeros += 1
                res += conseq_zeros
            else:
                conseq_zeros = 0
        return res
        




sol = Solution()
nums = [0,0,0,2,0,0]
res = sol.zeroFilledSubarray(nums)
print(f"zeroFilledSubarray {res}")
assert res == 9 
