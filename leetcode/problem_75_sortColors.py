from typing import List
from collections import Counter


class Solution:
    def sortColors(self, nums: List[int]) -> None:

        buckets = Counter(nums)

        idx = 0
        for bucket_nb in [0, 1, 2]:
            occurences = buckets[bucket_nb]
            for _ in range(occurences):
                nums[idx] = bucket_nb
                idx += 1
