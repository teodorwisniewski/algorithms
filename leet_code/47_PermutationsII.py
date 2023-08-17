from typing import List
from collections import Counter


# class Solution:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:

#         def backtrack(perm, idx, numbers):

#             if perm in res:
#                 return

#             if len(perm) == len(nums):
#                 res.append(perm.copy())
#                 return
#             prev = None
#             for i in range(len(numbers)):
#                 num = numbers[i]
#                 if prev == num:
#                     continue
#                 nums_without = numbers[:i] + numbers[i+1:]
#                 perm.append(num)
#                 backtrack(perm, i+1, nums_without)
#                 perm.pop()
#                 prev = num
    
#         res = []
#         nums.sort()
#         backtrack([], 0, nums)
#         return res



class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def backtrack():

            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for num in counted_nums:
                if not counted_nums[num]:
                    continue
                perm.append(num)
                counted_nums[num] -= 1
                backtrack()
                perm.pop()
                counted_nums[num] += 1
    
        res = []
        counted_nums = Counter(nums)
        perm = []
        backtrack()
        return res




s = Solution()

nums = [1, 1, 2]
res = s.permuteUnique(nums)
print(f"permuteUnique {res}")

