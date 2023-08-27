
from typing import List


def solveSudoku(board):
    solve_partial_sudoku(0, 0, board)
    return board


def solve_partial_sudoku(row_nb: int, col_nb: int, board: List) -> bool:

    curr_row = row_nb
    curr_col = col_nb

    if curr_col == len(board[0]):
        curr_row += 1
        curr_col = 0
        if curr_row == len(board):
            return True
        
    if board[curr_row][curr_col] == 0:
        return try_digits_at_pos(curr_row, curr_col, board)
    
    return solve_partial_sudoku(curr_row, curr_col+1, board)
    

def try_digits_at_pos(row_nb: int, col_nb: int, board: List) -> bool:

    for digit in range(1,10):
        if is_valid_at_pos(digit, row_nb, col_nb, board):
            board[row_nb][col_nb] = digit
            if solve_partial_sudoku(row_nb, col_nb+1, board):
                return True
        
    board[row_nb][col_nb] = 0
    return False


def is_valid_at_pos(val: int, row_nb: int, col_nb: int, board: List) -> bool:

    is_invalid_row = val in board[row_nb]
    is_invalid_col = val in map(lambda board: board[col_nb], board)

    if is_invalid_row or is_invalid_col:
        return False
    
    return is_absent_in_subgrid(val, row_nb, col_nb, board)


def is_absent_in_subgrid(val: int, row_nb: int, col_nb: int, board: List) -> bool:

    row_subgrid_start_idx = (row_nb // 3) * 3
    col_subgrid_start_idx = (col_nb // 3) * 3

    for row_step in range(3):
        for col_step in range(3):
            row_idx_to_check = row_subgrid_start_idx + row_step
            col_idx_to_check = col_subgrid_start_idx + col_step
            if board[row_idx_to_check][col_idx_to_check] == val:
                return False
    return True 


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