from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            
            right_sum = total - left_sum - num
            if left_sum == right_sum:
                return i
            left_sum += num
        

        return -1



sol = Solution()
nums = [1,7,3,6,5,6]
res = sol.pivotIndex(nums)
print(f"pivotIndex {res}")