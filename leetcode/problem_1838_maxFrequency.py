from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        nums.sort()
        total, res = 0, 0
        left, right = 0, 0

        while right < len(nums):
            total += nums[right]
            while nums[right]*(right-left+1) > (total + k):
                total -= nums[left]
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res

        
sol = Solution()
nums = [1,2,4]
k = 5
res = sol.maxFrequency(nums, k)
print(f'maxFrequency {res}')