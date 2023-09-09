
from typing import List





class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:


        results = []

        def dfs(idx, comb, total):

            if total == target:
                results.append(comb[:])
                return
            if idx >= len(candidates) or total > target:
                return
            
            curr_num = candidates[idx]
            comb.append(curr_num)
            dfs(idx, comb, total+curr_num)
            comb.pop()
            dfs(idx+1, comb, total)

        
        dfs(0, [], 0)
        return results
    

s = Solution()


candidates = [2, 3, 5]
target = 8
res = s.combinationSum(candidates, target)
print(f"combinationSum {res}")

candidates = [2]
target = 1
res = s.combinationSum(candidates, target)
print(f"combinationSum {res}")



