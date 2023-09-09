from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

        if k==1:
            return 0

        nums.sort()
        left, right = 0, k-1
        diff = float("inf")
        while right < len(nums):
            diff = min(diff, nums[right] - nums[left])
            left += 1
            right += 1

        return diff


        



sol = Solution()
nums = [9,4,1,7]
k = 2
res = sol.minimumDifference(nums, k)
print(f"minimumDifference {res}")
