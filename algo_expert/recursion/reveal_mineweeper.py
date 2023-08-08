from itertools import product


def revealMinesweeper(board, row, column):

    if row == 1 and column == 1:
        print(board)
    spot_val = board[row][column]
    if spot_val == "M":
        board[row][column] = "X"
        return board

    neighbors = get_neighbors(board, row, column)
    adjacent_mine_count = get_adjacent_mine_count(board, neighbors)
    if adjacent_mine_count:
        board[row][column] = str(adjacent_mine_count)
    else:
        board[row][column] = str(adjacent_mine_count)
        for neig_row, neig_col in neighbors:
            if board[neig_row][neig_col] == "H":
                revealMinesweeper(board, neig_row, neig_col) 
    return board


def get_neighbors(board, row, column):
    ROWS, COLS = len(board), len(board[0])
    directions = list(product([-1, 0, 1], repeat=2))
    neighbors = []
    for row_dir, col_dir in directions:
        new_row = row + row_dir
        new_col = column + col_dir
        if (
            0 <= new_row < ROWS and
            0 <= new_col < COLS
        ):
            neighbors.append((new_row, new_col))
    return neighbors


def get_adjacent_mine_count(board, neighbors):
    adjacent_mine_count = 0
    for row, col in neighbors:
        if board[row][col] == "M":
            adjacent_mine_count += 1
    return adjacent_mine_count


board = [
  ["M", "M"],
  ["H", "H"],
  ["H", "H"]
] 

row_nb = 2
col_nb = 0


# Print the board
for row in board:
    print(' '.join(row))


# Print the word
print("row:", row_nb, " col:", col_nb)
output_board = revealMinesweeper(board, row_nb, col_nb)

print("revealMinesweeper output")
for row in output_board:
    print(' '.join(row))

expected_output = [
  ["M", "M"],
  ["2", "2"],
  ["0", "0"]
]

assert output_board == expected_output