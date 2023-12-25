from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def backtrack(idx, comb):
            
            if comb not in res:
                res.append(comb.copy())

            prev = None
            for i in range(idx, len(nums)):
                num = nums[i]
                if prev == num:
                    continue
                comb.append(num)
                backtrack(i+1, comb)
                comb.pop()
                prev = num

        nums.sort()
        backtrack(0, [])
        return res






s = Solution()

nums = [1,2,2]
res = s.subsetsWithDup(nums)
print(f"subsetsWithDup {res}")

