
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0: -1}
        total = 0

        for idx, num in enumerate(nums):
            total += num
            r = total % k
            if r not in remainder:
                remainder[r] = idx
            elif (idx - remainder[r]) > 1:
                return True
            
        return False
  


sol = Solution()
# nums = [23,2,4,6,7]
# k = 6
# res = sol.checkSubarraySum(nums, k)
# print(f"checkSubarraySum {res}")

# nums = [2, 4, 3]
# k = 6
# res = sol.checkSubarraySum(nums, k)
# print(f"checkSubarraySum {res}")

# nums = [0]
# k = 1
# res = sol.checkSubarraySum(nums, k)
# print(f"checkSubarraySum {res}")

nums = [5, 0, 0, 0]
k = 3
res = sol.checkSubarraySum(nums, k)
print(f"checkSubarraySum {res}")