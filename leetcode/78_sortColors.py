from typing import List
from collections import Counter


# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         buckets = Counter(nums)

#         idx = 0
#         for bucket in range(3):
#             freq = buckets[bucket]
#             for _ in range(freq):
#                 nums[idx] = bucket
#                 idx += 1


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        idx = 0

        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        while idx <= right:

            if nums[idx] == 0:
                swap(left, idx)
                left += 1
                
            
            if nums[idx] == 2:
                swap(idx, right)
                right -= 1
                idx -= 1

            idx += 1
        



sol = Solution()

nums = [2, 0, 2, 1, 1, 0]
sol.sortColors(nums)
print(f"sortColors {nums}")