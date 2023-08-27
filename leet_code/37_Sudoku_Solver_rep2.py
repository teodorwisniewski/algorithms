from collections import defaultdict
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.is_solved = False
        self.track_existing_numbers()

        self.solve_partial_sudoku(0, 0)

    def track_existing_numbers(self):

        self.used_row_digits = [set() for _ in range(9)]
        self.used_col_digits = [set() for _ in range(9)]
        self.used_square_digits = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = self.board[r][c]
                if val != ".":
                    self.used_row_digits[r].add(val)
                    self.used_col_digits[c].add(val)
                    box_id = r//3 * 3 + c//3
                    self.used_square_digits[box_id].add(val)

    def solve_partial_sudoku(self, row_nb, col_nb):

        curr_row = row_nb
        curr_col = col_nb

        if curr_col == 9:
            curr_col = 0
            curr_row += 1
            if curr_row == 9:
                self.is_solved = True
                return
        
        if self.board[curr_row][curr_col] != ".":
            self.solve_partial_sudoku(curr_row, curr_col+1)
        else:
            for digit_candidate in range(1, 10):
                val = str(digit_candidate)
                if self.check_potential_candidate(val, curr_row, curr_col):
                    self.used_row_digits[curr_row].add(val)
                    self.used_col_digits[curr_col].add(val)
                    box_idx = curr_row//3 * 3 + curr_col//3
                    self.used_square_digits[box_idx].add(val)
                    self.board[curr_row][curr_col] = val
                    self.solve_partial_sudoku(curr_row, curr_col+1)
                    if not self.is_solved:
                        self.used_row_digits[curr_row].remove(val)
                        self.used_col_digits[curr_col].remove(val)
                        self.used_square_digits[box_idx].remove(val)
                        self.board[curr_row][curr_col] = "."
            
            self.board

    def check_potential_candidate(self, digit_candidate, curr_row, curr_col) -> bool: 

        is_invalid_row_candidate = digit_candidate in self.used_row_digits[curr_row]
        is_invalid_col_candidate = digit_candidate in self.used_col_digits[curr_col]
        box_idx = curr_row//3 * 3 + curr_col//3
        is_invalid_box_candidate = digit_candidate in self.used_square_digits[box_idx]

        if is_invalid_row_candidate or is_invalid_col_candidate or is_invalid_box_candidate:
            return False
        
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



sol.solveSudoku(board)
print(f"solveSudoku {board}")