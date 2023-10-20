from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        used_rows = defaultdict(set)
        used_cols = defaultdict(set)
        used_squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                
                value = board[row][col]
                # check if it is an empty square
                if value == ".":
                    continue

                square_id = (row//3, col//3)
                if (
                    value in used_rows[row] or
                    value in used_cols[col] or
                    value in used_squares[square_id]
                ):
                    return False
                
                used_rows[row].add(value)
                used_cols[col].add(value)
                used_squares[square_id].add(value)
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