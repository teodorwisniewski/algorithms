from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        target_side_length = sum(matchsticks) // 4
        sides = [0] * 4
        if sum(matchsticks)/4 != target_side_length:
            return False
        
        matchsticks.sort(reverse=True)

        def backtrack(idx, first_side):
            if idx == len(matchsticks):
                return True
            for i in range(4):
                if sides[i] + matchsticks[idx] < target_side_length:
                    sides[i] += matchsticks[idx]
                    
                    if backtrack(idx+1, first_side):
                        return True
                    # cleaning up
                    sides[i] -= matchsticks[idx]
                elif sides[i] + matchsticks[idx] == target_side_length:
                    sides[i] += matchsticks[idx]
                    if backtrack(idx+1, first_side+1):
                        return True
                    sides[i] -= matchsticks[idx]
            return False
        return backtrack(0, 0)




sol = Solution()

matchsticks = [1,1,2,2,2]
res = sol.makesquare(matchsticks)
print(f"makesquare {res}")


matchsticks = [3,3,3,3,4]
res = sol.makesquare(matchsticks)
print(f"makesquare {res}")
