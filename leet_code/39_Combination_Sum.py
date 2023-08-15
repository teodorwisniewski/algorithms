
from typing import List



# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
#         def backtrack(combs, comb):
#             comb_sum = sum(comb)
#             if comb in combs:
#                 return
#             elif comb_sum == target:
#                 combs.append(comb.copy())
#                 return
#             elif comb_sum > target:
#                 return
        
#             for num in candidates:
#                 if len(comb) == 0:
#                     print(num)
#                 comb.append(num) 
#                 comb.sort()
#                 backtrack(combs, comb)
#                 comb.remove(num)
#         results = []
#         backtrack(results, [])
#         return results

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(idx, comb, comb_sum):
            if comb_sum == target:
                results.append(comb.copy())
                return
            elif comb_sum > target or idx >= len(candidates):
                return
            
            new_num = candidates[idx]
            comb.append(new_num)
            backtrack(idx, comb, comb_sum + new_num)
            comb.pop()
            backtrack(idx+1, comb, comb_sum)

        results = []
        backtrack(0, [], 0)
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



