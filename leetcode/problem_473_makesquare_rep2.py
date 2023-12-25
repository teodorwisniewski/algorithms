from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        n = len(matchsticks)
        perimeter = sum(matchsticks)
        target_side, r = divmod(perimeter, 4)
        if r:
            return False
        matchsticks.sort(reverse=True)
        sides = [0] * 4

        def dfs(idx):
            if idx == n:
                if len(set(sides)) == 1:
                    return True
                else:
                    return False
            
            matchstick_len = matchsticks[idx]
            
            for j in range(4):
                if sides[j] + matchsticks[idx] > target_side:
                    continue

                sides[j] += matchstick_len
                if dfs(idx+1):
                    return True
                sides[j] -= matchstick_len
                if not sides[j]: break
            return False
        
        return dfs(0)



sol = Solution()

matchsticks = [1,1,2,2,2]
res = sol.makesquare(matchsticks)
print(f"makesquare {res}")


matchsticks = [3,3,3,3,4]
res = sol.makesquare(matchsticks)
print(f"makesquare {res}")
