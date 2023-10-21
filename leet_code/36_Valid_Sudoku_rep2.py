from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        used_rows = defaultdict(set)
        used_cols = defaultdict(set)
        used_squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                square_idx = (r//3, c//3)
                if (
                    val in used_rows[r] or
                    val in used_cols[c] or
                    val in used_squares[square_idx]
                ):
                    return False
                
                used_rows[r].add(val)
                used_cols[c].add(val)
                used_squares[square_idx].add(val)

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