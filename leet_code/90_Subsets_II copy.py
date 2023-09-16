from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        n = len(nums)
        nums.sort()

        def backtrack(idx: int, subset: List):

            if idx == n:
                res.append(subset[:])
                return

            # All subsets that include nums[idx]
            curr_num = nums[idx]
            subset.append(curr_num)
            backtrack(idx+1, subset)
            subset.pop()

            # All subsets that don't include nums[idx]
            while idx + 1 < len(nums) and curr_num == nums[idx+1]:
                idx += 1
            
            backtrack(idx+1, subset)

        backtrack(0, [])
        return res




s = Solution()

nums = [1,2,2]
res = s.subsetsWithDup(nums)
print(f"subsetsWithDup {res}")

