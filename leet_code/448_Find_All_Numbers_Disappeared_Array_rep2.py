from typing import List

# class Solution:
#     def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
#         # mapping
#         for num in nums:
#             new_idx = abs(num) - 1
#             nums[new_idx] = -1 * abs(nums[new_idx])

#         res = []
#         for idx, num in enumerate(nums):
#             if num > 0:
#                 res.append(idx+1)
#         return res
    

# class Solution:
#     def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
#         hash_set = set(nums)

#         res = []
#         for idx in range(1, len(nums)+1):
#             if idx not in hash_set:
#                 res.append(idx)

#         return res
    
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        
        
        return set(range(1, len(nums)+1)) - set(nums)

sol = Solution()

nums = [4, 3, 2, 7, 8, 2, 3, 1]
res = sol.findDisappearedNumbers(nums)
print(f"findDisappearedNumbers {res}")