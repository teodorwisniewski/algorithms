from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(comb, total, idx):

            if total == target and comb not in res:
                res.append(comb.copy())
            if total >= target:
                return

            prev = None
            for i in range(idx, len(candidates)):
                num = candidates[i] 
                if prev == num:
                    continue
                comb.append(num)
                backtrack(comb, total+num, i+1)
                comb.pop()
                prev = num
                
        candidates = sorted(candidates)
        res = []
        backtrack([], 0, 0)
        return res





s = Solution()

candidates = [10,1,2,7,6,1,5]
target = 8
res = s.combinationSum2(candidates, target)
print(f"combinationSum2 {res}")

