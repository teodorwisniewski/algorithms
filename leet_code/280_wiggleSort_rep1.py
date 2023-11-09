from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        
        for idx in range(1, len(nums)):

            if (
                (idx % 2 == 1 and nums[idx] < nums[idx - 1]) or
                (idx % 2 == 0 and nums[idx] > nums[idx - 1])
            ):
                nums[idx], nums[idx - 1] = nums[idx - 1], nums[idx]

        return nums 
    
sol = Solution()
nums = [3, 5, 2, 1, 6, 4]
res = sol.wiggleSort(nums)
print(f"res {res}")