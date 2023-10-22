from typing import List
from collections import Counter


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = Counter(nums)

        idx = 0
        for bucket in range(3):
            freq = buckets[bucket]
            for _ in range(freq):
                nums[idx] = bucket
                idx += 1
        return nums




sol = Solution()

nums = [2, 0, 2, 1, 1, 0]
res = sol.sortColors(nums)
print(f"sortColors {res}")