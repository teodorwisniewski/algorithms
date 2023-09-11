
from typing import Optional, List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []

        def backtrack(start, comb):
            if len(comb) == k:
                res.append(comb.copy())
                return
            for i in range(start, n+1):
                comb.append(i)
                backtrack(i+1, comb)
                comb.pop()
        backtrack(1, [])
        return res


s = Solution()

res = s.combine(4, 2)
print(f"combine {res}")


res = s.combine(1, 1)
print(f"combine {res}")
