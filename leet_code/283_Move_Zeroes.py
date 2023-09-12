from typing import List



class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        p_l = 0
        for p_r in range(len(nums)):
            if nums[p_r]:
                nums[p_l], nums[p_r] = nums[p_r], nums[p_l]
                p_l += 1
            
                 
                
        


nums = [0,1,0,3,12]

sol = Solution()

sol.moveZeroes(nums)
print(f"moveZeroes {nums}")