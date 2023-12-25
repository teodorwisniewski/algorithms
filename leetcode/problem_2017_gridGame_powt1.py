from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:

        N = len(grid[0])
        pref_row_1, pref_row_2 = grid[0].copy(), grid[1].copy()

        for i in range(1, N):
            pref_row_1[i] += pref_row_1[i - 1]
            pref_row_2[i] += pref_row_2[i - 1]

        res = float("inf")
        for i in range(N):
            top = pref_row_1[-1] - pref_row_1[i]
            bottom = pref_row_2[i-1] if i > 0 else 0
            res_robot_2 = max(top, bottom)
            res = min(res, res_robot_2)
        return res


    
grid = [
        [2,5,4],        
        [1,5,1]
        ]
sol = Solution()
res = sol.gridGame(grid)
print(f"gridGame {res}")
