from typing import Optional, List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        results = []
        
        def dfs(idx, subset):
            
            if idx == len(nums):
                results.append(subset.copy())
                return

            # include the number
            subset.append(nums[idx])
            dfs(idx+1, subset)

            # exclude the number
            subset.pop()
            dfs(idx+1, subset)

        dfs(0, [])
        return results

s = Solution()

res = s.subsets([1, 2, 3])
print(f"subsets {res}")


res = s.subsets([4,1,0])
print(f"\n subsets {res}")