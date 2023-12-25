

from typing import List


# class Solution:
#     # TC O(n) SC O(n)
#     def firstMissingPositive(self, nums: List[int]) -> int:

#         nums_set = set(nums)
#         for i in range(len(nums)):
#             if i+1 in nums_set:
#                 continue
#             return i+1
#         return len(nums)+1
        

class Solution:
    # TC O(n) SC O(1)
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # replace all negative numbers
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0
        
        for i in range(n):
            new_idx = abs(nums[i]) - 1
            if new_idx < 0 or new_idx >= n:
                nums[i] *= 0
                continue
            if not nums[new_idx]:
                nums[new_idx] = -1 * abs(nums[i])
            else:
                nums[new_idx] = -1 * abs(nums[new_idx])

        for i in range(n):
            if nums[i] >= 0:
                return i+1
        
        return n + 1




sol = Solution()
nums = [7, 8, 9, 11, 12] # [1, 2, 0]
res = sol.firstMissingPositive(nums)
print(f"firstMissingPositive {res}")


nums = [3,4,-1,1] # [1, 2, 0]
res = sol.firstMissingPositive(nums)
print(f"firstMissingPositive {res}")
