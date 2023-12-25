from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:

        N = len(grid[0])
        prefix_row_1 = grid[0].copy()
        prefix_row_2 = grid[1].copy()       

        for i in range(1, N):
            prefix_row_1[i] += prefix_row_1[i - 1]
            prefix_row_2[i] += prefix_row_2[i - 1]
        
        res = float("inf")

        for i in range(N):
            top = prefix_row_1[-1] - prefix_row_1[i]
            bottom = prefix_row_2[i-1] if i > 0 else 0
            second_rob_res = max(top, bottom)
            res = min(res, second_rob_res)
        return res


    
grid = [
        [2,5,4],        
        [1,5,1]
        ]
sol = Solution()
res = sol.gridGame(grid)
print(f"gridGame {res}")
