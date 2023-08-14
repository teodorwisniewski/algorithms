from typing import Optional, List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        results = [[]]

        def backtrack(subset):

            if subset not in results:
                results.append(subset.copy())
                return
            
            if len(nums) < len(subset):
                return 
       

            for sub in results:
                for num in nums:
                    new_subset = sorted(sub + [num])
                    if new_subset in results or num in sub:
                        continue
                    backtrack(new_subset)
        backtrack([])
        return results
    

s = Solution()

res = s.subsets([1, 2, 3])
print(f"subsets {res}")


res = s.subsets([4,1,0])
print(f"\n subsets {res}")