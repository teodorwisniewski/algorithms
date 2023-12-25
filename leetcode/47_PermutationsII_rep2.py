from typing import List
from collections import Counter




class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        counter = Counter(nums)
        n = len(nums)
        results = []

        def backtrack(perm):

            if len(perm) == n:
                results.append(perm[:])

            for num in counter:
                if not counter[num]:
                    continue
                counter[num] -= 1
                perm.append(num)
                backtrack(perm)
                counter[num] += 1
                perm.pop()
        
        backtrack([])
        return results

        




        





s = Solution()

nums = [1, 1, 2]
res = s.permuteUnique(nums)
print(f"permuteUnique {res}")

