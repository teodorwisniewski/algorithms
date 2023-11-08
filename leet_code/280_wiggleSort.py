from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        
        for idx in range(1, len(nums)):
            prev_val = nums[idx - 1]
            curr_val = nums[idx]
            cond1 = (
                idx % 2 == 1 and curr_val < prev_val
            )
            cond2 = (
                idx % 2 == 0 and curr_val > prev_val
            )
            if cond1 or cond2:
                nums[idx], nums[idx - 1] = prev_val, curr_val

        return nums
        



sol = Solution()
nums = [3,5,2,1,6,4]
res = sol.wiggleSort(nums)
print(f"res {res}")