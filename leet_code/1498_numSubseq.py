
from typing import List


# class Solution:
#     def numSubseq(self, nums: List[int], target: int) -> int:
#         nums.sort()
#         res = 0
#         mod = 10**9 + 7

#         right_pointer = len(nums) - 1 
#         for left_pointer, left_value in enumerate(nums):
#             while (left_value + nums[right_pointer] > target and
#                    left_pointer <= right_pointer):
#                 right_pointer -= 1
#             if left_pointer <= right_pointer:
#                 res += 2**(right_pointer - left_pointer)
#                 res %= mod
#         return res


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        mod = 10**9 + 7

        right_pointer = len(nums) - 1 
        left_pointer = 0
        while left_pointer <= right_pointer:
            if nums[left_pointer] + nums[right_pointer] > target:
                right_pointer -= 1
            else :
                res += pow(2, right_pointer - left_pointer, mod)
                left_pointer += 1
    
        return res % mod



sol = Solution()

nums = [3,5,6,7]
target = 9
res = sol.numSubseq(nums, target)
print(f"numSubseq {res}")
assert res == 4


nums = [2,3,3,4,6,7]
target = 12
res = sol.numSubseq(nums, target)
print(f"numSubseq {res}")
assert res == 61
        
        