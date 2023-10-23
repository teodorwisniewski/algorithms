from typing import List
from collections import Counter


# class Solution:
#     def sortColors(self, nums: List[int]) -> None:

#         map_colors = Counter(nums)

#         idx = 0
#         for color in range(3):
#             freq = map_colors[color]
#             for _ in range(freq):
#                 nums[idx] = color
#                 idx += 1


class Solution:
    def sortColors(self, nums: List[int]) -> None:

        l, r = 0, len(nums) - 1
        idx = 0

        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        while idx <= r:

            if nums[idx] == 0:
                swap(l, idx)
                l += 1
            
            if nums[idx] == 2:
                swap(r, idx)
                r -= 1
                idx -= 1
            
            idx += 1






sol = Solution()

nums = [2, 0, 2, 1, 1, 0]
sol.sortColors(nums)
print(f"sortColors {nums}")