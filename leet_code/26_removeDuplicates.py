from typing import List


# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:

#         left = 0
#         last_val = nums[0]
#         for r in range(1, len(nums)):
#             new_val = nums[r]
#             if new_val != last_val:
#                 left += 1
#                 last_val = new_val
#                 nums[left] = new_val

#         return left + 1



class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        left = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[left] = nums[r]
                left += 1 
        return left 
        
        



sol = Solution()

nums = [0,0,1,1,1,2,2,3,3,4]
res = sol.removeDuplicates(nums)
print(f"removeDuplicates {res}")
print(f"removeDuplicates {nums}")
