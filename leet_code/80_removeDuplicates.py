from typing import List


# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> 



class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        left, right = 0, 0
        n = len(nums)
        while right < n:

            count = 1
            while right+1 < n and nums[right] == nums[right+1]:
                right += 1
                count += 1
            
            for _ in range(min(2, count)):
                nums[left] = nums[right]
                left += 1
            right += 1

        return left


sol = Solution()

nums = [1,1,1,2,2, 2, 2,3]
res = sol.removeDuplicates(nums)
print(f"removeDuplicates {res}")
print(f"removeDuplicates {nums}")
