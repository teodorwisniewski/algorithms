from typing import List



class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[left], nums[r] = nums[r], nums[left]
                left += 1
        return nums
            
            
                 
                
        


nums = [0,1,0,3,12]

sol = Solution()

sol.moveZeroes(nums)
print(f"moveZeroes {nums}")