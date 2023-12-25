from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res = []
        used_pos_diag = set()
        used_neg_diag = set()
        used_cols = set()
        board = [["."] * n for i in range(n)]

        def backtrack(row_nb: int):

            if row_nb == n:
                solution = ["".join(row) for row in board]
                res.append(solution)
                return
            
            for col in range(n):
                cond = (
                    col in used_cols or
                    (row_nb + col) in used_pos_diag or
                    (row_nb - col) in used_neg_diag
                )
                if cond:
                    continue

                used_cols.add(col)
                used_pos_diag.add(row_nb + col)
                used_neg_diag.add(row_nb - col)
                board[row_nb][col] = "Q"
                backtrack(row_nb+1)
                used_cols.remove(col)
                used_pos_diag.remove(row_nb + col)
                used_neg_diag.remove(row_nb - col)
                board[row_nb][col] = "."
                
        backtrack(0)
        return res





s = Solution()
n = 4
res = s.solveNQueens(n)
print(f"solveNQueens {res}")
