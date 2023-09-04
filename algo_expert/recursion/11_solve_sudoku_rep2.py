
from typing import List


class SudokuBoard:

    def __init__(self, board: List):
        self.board = board
        self.is_solved = False
        self.track_used_fields()

    def track_used_fields(self):

        self.used_rows_numbers = [set() for _ in range(9)]
        self.used_cols_numbers = [set() for _ in range(9)]
        self.used_squares_numbers = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                field_value = self.board[r][c]
                if field_value not in [0, "."]:
                    self.track_digit(r, c, field_value)

    def get_box_id(self, row, col):
        return row//3 * 3 + col // 3

    def track_digit(self, row, col, value):
        self.used_rows_numbers[row].add(value)
        self.used_cols_numbers[col].add(value)
        box_id = self.get_box_id(row, col)
        self.used_squares_numbers[box_id].add(value)

    def place_digit(self, row, col, value):
        self.track_digit(row, col, value)
        self.board[row][col] = value

    def remove_digit_from_board(self, row, col, value):
        self.used_rows_numbers[row].remove(value)
        self.used_cols_numbers[col].remove(value)
        box_id = self.get_box_id(row, col)
        self.used_squares_numbers[box_id].remove(value)
        self.board[row][col] = 0

    def is_valid_digit_at_pos(self, row, col, digit):
        box_id = self.get_box_id(row, col)
        cond = (
            digit in self.used_rows_numbers[row] or
            digit in self.used_cols_numbers[col] or
            digit in self.used_squares_numbers[box_id]
        )
        if cond:
            return False

        return True


def solve_partial_sudoku(row_nb, col_nb, board: SudokuBoard):

    if col_nb == 9:
        row_nb += 1
        if row_nb == 9:
            board.is_solved = True
            return 
        col_nb = 0

    if board.board[row_nb][col_nb] == 0:
        try_digit_at_pos(row_nb, col_nb, board)
    else:
        solve_partial_sudoku(row_nb, col_nb+1, board)


def try_digit_at_pos(row_nb, col_nb, board: SudokuBoard):

    for digit in range(1, 10):
        if board.is_valid_digit_at_pos(row_nb, col_nb, digit):
            board.place_digit(row_nb, col_nb, digit)
            solve_partial_sudoku(row_nb, col_nb+1, board)
            if not board.is_solved:
                board.remove_digit_from_board(row_nb, col_nb, digit)
            else:
                return


def solveSudoku(board):
    sudoku_board = SudokuBoard(board)
    solve_partial_sudoku(0, 0, sudoku_board)
    return board





input = [
  [7, 8, 0, 4, 0, 0, 1, 2, 0],
  [6, 0, 0, 0, 7, 5, 0, 0, 9],
  [0, 0, 0, 6, 0, 1, 0, 7, 8],
  [0, 0, 7, 0, 4, 0, 2, 6, 0],
  [0, 0, 1, 0, 5, 0, 9, 3, 0],
  [9, 0, 4, 0, 6, 0, 0, 0, 5],
  [0, 7, 0, 3, 0, 0, 0, 1, 2],
  [1, 2, 0, 0, 0, 7, 4, 0, 0],
  [0, 4, 9, 2, 0, 6, 0, 0, 7],
]

expected_output = [
  [7, 8, 5, 4, 3, 9, 1, 2, 6],
  [6, 1, 2, 8, 7, 5, 3, 4, 9],
  [4, 9, 3, 6, 2, 1, 5, 7, 8],
  [8, 5, 7, 9, 4, 3, 2, 6, 1],
  [2, 6, 1, 7, 5, 8, 9, 3, 4],
  [9, 3, 4, 1, 6, 2, 7, 8, 5],
  [5, 7, 8, 3, 9, 4, 6, 1, 2],
  [1, 2, 6, 5, 8, 7, 4, 9, 3],
  [3, 4, 9, 2, 1, 6, 8, 5, 7],
]


res = solveSudoku(input)
print(f"solveSudoku {res}")

assert res == expected_output