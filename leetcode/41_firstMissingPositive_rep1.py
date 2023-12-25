

from typing import List


# class Solution:
#     # TC O(n) SC O(n)
#     def firstMissingPositive(self, nums: List[int]) -> int:

#         nums_set = set(nums)
#         for i in range(len(nums)):
#             if i+1 in nums_set:
#                 continue
#             return i+1
#         return len(nums)+1
        

class Solution:
    # TC O(n) SC O(1)
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for idx in range(n):
            if nums[idx] < 0:
                nums[idx] = 0

        for idx in range(n):
            value = abs(nums[idx])
            mapped_idx = value - 1
            if 1 <= value <= n:
                if nums[mapped_idx] > 0:
                    nums[mapped_idx] *= -1
                elif nums[mapped_idx] == 0:
                    nums[mapped_idx] = -(n+1)

 
        for idx in range(n):
            if nums[idx] >= 0:
                return idx+1

        return n + 1




sol = Solution()


nums = [1,2,0]
res = sol.firstMissingPositive(nums)
print(f"firstMissingPositive {res}")



nums = [7, 8, 9, 11, 12] # [1, 3, 2]
res = sol.firstMissingPositive(nums)
print(f"firstMissingPositive {res}")


nums = [3,4,-1,1] # [1, 2, 0]
res = sol.firstMissingPositive(nums)
print(f"firstMissingPositive {res}")
