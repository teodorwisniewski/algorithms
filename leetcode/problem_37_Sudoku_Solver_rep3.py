from collections import defaultdict
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        self.board = board
        self.is_solved = False
        self.get_used_numbers()
        self.solve_patrial_sudoku(0, 0)
        return self.board
        
    def solve_patrial_sudoku(self, row_nb, col_nb):
        
        if col_nb == 9:
            row_nb += 1
            if row_nb == 9:
                self.is_solved = True
                return 
            col_nb = 0
        
        if self.board[row_nb][col_nb] == ".":
            self.try_digit_at_pos(row_nb, col_nb)
        else:
            self.solve_patrial_sudoku(row_nb, col_nb+1)

    def try_digit_at_pos(self, row_nb, col_nb):

        for val in range(1, 10):
            digit = str(val)
            if self.is_valid_digit_at_pos(row_nb, col_nb, digit):
                self.place_digit(row_nb, col_nb, digit)
                self.board[row_nb][col_nb] = digit
                self.solve_patrial_sudoku(row_nb, col_nb+1)
                if not self.is_solved:
                    self.remove_digit(row_nb, col_nb, digit)
                else:
                    return
        # cleaning
        self.board[row_nb][col_nb] = "."

    def is_valid_digit_at_pos(self, row_nb, col_nb, digit):

        if digit in self.used_row_nbs[row_nb]:
            return False

        if digit in self.used_col_nbs[col_nb]:
            return False
        
        box_id = row_nb//3 * 3 + col_nb//3
        if digit in self.used_square_nbs[box_id]:
            return False

        return True
        
    def get_used_numbers(self):
        self.used_row_nbs = [set() for _ in range(9)]
        self.used_col_nbs = [set() for _ in range(9)]
        self.used_square_nbs = [set() for _ in range(9)]

        for row_idx in range(9):
            for col_idx in range(9):
                val = self.board[row_idx][col_idx]
                if val != ".":
                    self.place_digit(row_idx, col_idx, val)

    def place_digit(self, row_idx, col_idx, val):
        box_idx = row_idx//3 * 3 + col_idx//3
        self.used_row_nbs[row_idx].add(val)
        self.used_col_nbs[col_idx].add(val)
        self.used_square_nbs[box_idx].add(val)

    def remove_digit(self, row_idx, col_idx, val):
        box_idx = row_idx//3 * 3 + col_idx//3
        self.used_row_nbs[row_idx].remove(val)
        self.used_col_nbs[col_idx].remove(val)
        self.used_square_nbs[box_idx].remove(val)





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