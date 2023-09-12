from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        n = len(matchsticks)
        perimeter = sum(matchsticks)
        if perimeter % 4 != 0:
            return False
        
        target_side = perimeter // 4

        def dfs(a, b, c, d, k):
            if k == n:
                if a == b == c == d == target_side:
                    return True
                else:
                    return False
            
            matchstick_len = matchsticks[k]
            if (
                a + matchstick_len <= target_side
                and dfs(a+matchstick_len, b, c, d, k+1)
            ):
                return True
            if (
                b + matchstick_len <= target_side
                and dfs(a, b+matchstick_len, c, d, k+1)
            ):
                return True
            if (
                c + matchstick_len <= target_side
                and dfs(a, b, c+matchstick_len, d, k+1)
            ):
                return True
            if (
                d + matchstick_len <= target_side
                and dfs(a, b, c, d+matchstick_len, k+1)
            ):
                return True
            return False
        return dfs(0, 0, 0, 0, 0)



sol = Solution()

matchsticks = [1,1,2,2,2]
res = sol.makesquare(matchsticks)
print(f"makesquare {res}")


matchsticks = [3,3,3,3,4]
res = sol.makesquare(matchsticks)
print(f"makesquare {res}")
