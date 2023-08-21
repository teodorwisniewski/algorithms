
from typing import List
from math import floor

class Solution:
    def getFactors(self, n: int) -> List[List[int]]:

        if n == 1:
            return []
        
        res = []

        def backtrack(comb, idx, product):
            
            if product == n:
                res.append(comb.copy())
                return

            if product > n:
                return
            
            end_idx = n // product + 1
            for factor in range(idx, end_idx):

                if (n % factor) == 0 and factor != n:
                    comb.append(factor)
                    backtrack(comb, factor, product*factor)
                    comb.pop()


        backtrack([], 2, 1)
        return res
        


s = Solution()
res = s.getFactors(12)
print(f"getFactors {res}")
