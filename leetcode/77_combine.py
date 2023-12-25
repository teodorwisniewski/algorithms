
from typing import Optional, List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        nums = list(range(1, n+1))
        def backtrack(idx, combs, comb):

            if len(comb) == k:
                combs.append(comb.copy())
                return
            
            for i in range(idx, len(nums)):
                num = nums[i]
                comb.append(num)
                backtrack(i+1, combs, comb)
                comb.pop()
        
        results = []
        backtrack(0, results, [])
        return results


s = Solution()

res = s.combine(4, 2)
print(f"combine {res}")


res = s.combine(1, 1)
print(f"combine {res}")
