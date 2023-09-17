

def revealMinesweeper(board, row, column):
    if board[row][column] == "M":
        board[row][column] = "X"
        return board
    return solvePartialMinesweeper(board, row, column)


def solvePartialMinesweeper(board, row, column):

    neighbors = get_neighbors(board, row, column)
    nb_adjacent_mines = 0
    for neig_row, neig_col in neighbors:
        if board[neig_row][neig_col] == "M":
            nb_adjacent_mines += 1

    if nb_adjacent_mines:
        board[row][column] = str(nb_adjacent_mines)
        return board

    board[row][column] = "0"
    for neig_row, neig_col in neighbors:
        if board[neig_row][neig_col] == "H":
            solvePartialMinesweeper(board, neig_row, neig_col)

    return board


def get_neighbors(board, row, column):

    potential_delta_steps = [-1, 0, 1]
    deltas = [
        (delta_x, delta_y) for delta_y in potential_delta_steps
        for delta_x in potential_delta_steps
        if not (delta_x == 0 and delta_y == 0)
    ]
    neighbors = []
    for delta_x, delta_y in deltas:

        new_x = row + delta_x
        new_y = column + delta_y
        if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]):
            neighbors.append((new_x, new_y))
    return neighbors
    





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