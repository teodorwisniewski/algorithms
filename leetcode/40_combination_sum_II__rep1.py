from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        results = []

        def backtrack(comb, start, target):

            if target == 0:
                results.append(comb[:])
                return

            if target < 0:
                return -1
            
            prev = None
            for idx in range(start, len(candidates)):
                candidate = candidates[idx]
                if candidate == prev:
                    continue

                comb.append(candidate)
                backtrack(comb, idx + 1, target - candidate)
                comb.pop()
                prev = candidate

        backtrack([], 0, target)
        return results




s = Solution()

candidates = [10,1,2,7,6,1,5]
target = 8
res = s.combinationSum2(candidates, target)
print(f"combinationSum2 {res}")

