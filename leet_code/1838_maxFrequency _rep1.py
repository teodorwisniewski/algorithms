from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        left, right = 0, 0
        res, total = 0, 0

        while right < len(nums):
            total += nums[right]
            potential_max_freq = nums[right]
            while (right - left + 1) * potential_max_freq > (k + total):
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