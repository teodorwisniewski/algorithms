from typing import List
from collections import Counter

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(comb, remain, cand_idx, counter):

            if remain == 0:
                res.append(comb.copy())
                return

            if remain < 0:
                return
            
            for next_cand_idx in range(cand_idx, len(counter)):
                potential_candidate, freq = counter[next_cand_idx]
                if freq <= 0:
                    continue
                counter[next_cand_idx] = (potential_candidate, freq-1)
                comb.append(potential_candidate)
                backtrack(comb, remain-potential_candidate, next_cand_idx, counter)
                counter[next_cand_idx] = (potential_candidate, freq)
                comb.pop()

        counter = Counter(candidates)
        counter = [(c, counter[c]) for c in counter]
        res = []
        backtrack([], target, 0, counter)
        return res





s = Solution()

candidates = [1,2,7,6,1,5, 10]
target = 8
res = s.combinationSum2(candidates, target)
print(f"combinationSum2 {res}")

