from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        NUMBERS = list(range(1,10))
        res = []

        def backtrack(comb, idx, total):

            if len(comb) != k and total == n:
                return

            if total == n:
                res.append(comb.copy())
                return
            
            for i in range(idx, len(NUMBERS)):
                num = NUMBERS[i]
                total  += num
                if total > n:
                    break
                comb.append(num)
                backtrack(comb, i+1, total)
                comb.pop()
                total -= num

        backtrack([], 0, 0)
        return res


s = Solution()
k = 3
n = 7
res = s.combinationSum3(k ,n)
print(f"combinationSum3 {res}")
