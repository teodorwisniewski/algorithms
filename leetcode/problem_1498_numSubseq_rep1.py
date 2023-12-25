
from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod = 10**9 + 7
        res = 0

        right_p = len(nums) - 1
        for left_p, left_val in enumerate(nums):

            while right_p > left_p and (left_val + nums[right_p] > target):
                right_p -= 1
            if (left_p <= right_p and 
                ((left_val + nums[right_p] <= target))
                ):
                res += pow(2, right_p-left_p, mod)
        return res % mod


sol = Solution()

nums = [3, 5, 6, 7]
target = 9
res = sol.numSubseq(nums, target)
print(f"numSubseq {res}")
assert res == 4


nums = [2, 3, 3, 4, 6, 7]
target = 12
res = sol.numSubseq(nums, target)
print(f"numSubseq {res}")
assert res == 61


nums = [1]
target = 1
res = sol.numSubseq(nums, target)
print(f"numSubseq {res}")
assert res == 0
        
        