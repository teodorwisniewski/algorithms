from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows_values = defaultdict(set)
        column_values = defaultdict(set)
        square_values = defaultdict(set)

        for r in range(9):
            for c in range(9):
                cell_val = board[r][c]
                if cell_val == ".":
                    continue
                cond = (
                    cell_val in rows_values[r] or
                    cell_val in column_values[c] or
                    cell_val in square_values[(r//3, c//3)]
                )
                if cond:
                    return False
                
                rows_values[r].add(cell_val)
                column_values[c].add(cell_val)
                square_values[(r//3, c//3)].add(cell_val)

        return True



sol = Solution()
board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

res = sol.isValidSudoku(board)
print(res)