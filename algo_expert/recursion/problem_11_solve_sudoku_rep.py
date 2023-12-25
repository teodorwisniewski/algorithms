
from typing import List


def solveSudoku(board):

    used_rows, used_cols, used_squares = get_existing_digits(board)
    is_solved = False

    def solve_partial_sudoku(row_nb, col_nb) -> bool:
        nonlocal is_solved
        curr_row = row_nb
        curr_col = col_nb

        if curr_col == 9:
            curr_col = 0
            curr_row += 1
            if curr_row == 9:
                is_solved = True
                return is_solved
        
        if board[curr_row][curr_col] == 0:
            try_digit_at_pos(curr_row, curr_col)
        else:
            solve_partial_sudoku(curr_row, curr_col+1)


    def try_digit_at_pos(row_nb, col_nb):
        for digit in range(1, 10):
            if is_valid_at_pos(digit, row_nb, col_nb):
                square_id = row_nb//3 * 3 + col_nb // 3
                used_rows[row_nb].add(digit)
                used_cols[col_nb].add(digit)
                used_squares[square_id].add(digit)
                board[row_nb][col_nb] = digit
                solve_partial_sudoku(row_nb, col_nb+1)
                if is_solved:
                    break
                used_rows[row_nb].remove(digit)
                used_cols[col_nb].remove(digit)
                used_squares[square_id].remove(digit)
                board[row_nb][col_nb] = 0


    def is_valid_at_pos(digit, row_nb, col_nb):
        square_id = row_nb//3 * 3 + col_nb // 3
        cond = (
            digit not in used_rows[row_nb] and
            digit not in used_cols[col_nb] and
            digit not in used_squares[square_id]
        )
        return cond
    solve_partial_sudoku(0, 0)
    return board


def get_existing_digits(board):

    used_rows = [set() for _ in range(9)]
    used_cols = [set() for _ in range(9)]
    used_squares = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val != 0:
                used_rows[r].add(val)
                used_cols[c].add(val)
                square_id = r//3 * 3 + c//3
                used_squares[square_id].add(val)

    return used_rows, used_cols, used_squares


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