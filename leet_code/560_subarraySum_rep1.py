
from typing import List
from collections import defaultdict



class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1
        cumulative_sum = 0

        for num in nums:
            cumulative_sum += num
            diff = cumulative_sum - k
            if diff in prefix_sums:
                res += prefix_sums[diff]
            prefix_sums[cumulative_sum] += 1
        return res





sol = Solution()
inputs = [1, -1, 1, 1, 1, 1]
res = sol.subarraySum(inputs, 3)
print(f"subarraySum {res}")