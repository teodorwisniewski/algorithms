from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def backtrack(perm, idx, numbers):

            if perm in res:
                return

            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for i in range(len(numbers)):
                num = numbers[i]
                nums_without = numbers[:i] + numbers[i+1:]
                perm.append(num)
                backtrack(perm, i+1, nums_without)
                perm.pop()
    
        res = []
        backtrack([], 0, nums)
        return res




s = Solution()

nums = [1, 1, 2]
res = s.permuteUnique(nums)
print(f"permuteUnique {res}")

