from typing import List
from collections import Counter


# class Solution:
#     def sortColors(self, nums: List[int]) -> None:

#         buckets = Counter(nums)

#         idx = 0
#         for bucket_nb in [0, 1, 2]:
#             occurences = buckets[bucket_nb]
#             for _ in range(occurences):
#                 nums[idx] = bucket_nb
#                 idx += 1



class Solution:
    def sortColors(self, nums: List[int]) -> None:

        lp, rp = 0, len(nums)-1

        def swap(idx1, idx2):
            nums[idx1], nums[idx2] = nums[idx2], nums[idx1]

        idx = 0

        while idx <= rp:

            if nums[idx] == 0:
                swap(idx, lp)
                lp += 1

            if nums[idx] == 2:
                swap(idx, rp)
                rp -= 1      
                idx -= 1

            idx += 1      
