
from typing import List
from collections import defaultdict



class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        res = 0
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        current_sum = 0

        for num in nums:
            current_sum += num
            diff = current_sum - k
            res += prefix_sum[diff]
            prefix_sum[current_sum] += 1
        return res





sol = Solution()
inputs = [1, -1, 1, 1, 1, 1]
res = sol.subarraySum(inputs, 3)
print(f"subarraySum {res}")