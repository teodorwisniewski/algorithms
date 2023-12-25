from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        target_side_len, rem = divmod(sum(matchsticks), 4)
        if rem:
            return False

        sides = [0] * 4
        matchsticks.sort(reverse=True)

        if matchsticks[0] > target_side_len:
            return False

        
        def dfs(idx):

            if idx == len(matchsticks):
                if len(set(sides)) == 1:
                    return True
                else:
                    return False
                
            matchstick = matchsticks[idx]
            for i in range(4):
                if sides[i] + matchstick > target_side_len:
                    continue
                sides[i] += matchstick
                if dfs(idx+1):
                    return True
                sides[i] -= matchstick
                if not sides[i]:
                    break
            return False

        return dfs(0)




sol = Solution()

matchsticks = [1,1,2,2,2]
res = sol.makesquare(matchsticks)
print(f"makesquare {res}")


matchsticks = [3,3,3,3,4]
res = sol.makesquare(matchsticks)
print(f"makesquare {res}")
