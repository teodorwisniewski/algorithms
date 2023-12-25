



from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        results = []
        def backtrack(perm, left_nums):

            if len(perm) == n:
                results.append(perm.copy())
                return
            
            for idx in range(len(left_nums)):
                perm.append(left_nums[idx])
                new_left_nums = left_nums[:idx] + left_nums[idx+1:]
                
                backtrack(perm, new_left_nums)
                perm.pop()
        
        backtrack([], nums)
        return results




s = Solution()

nums = [1, 2, 3]
res = s.permute(nums)
print(f"permute {res}")

