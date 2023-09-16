from itertools import product


def revealMinesweeper(board, row, column):

    if board[row][column] == "M":
        board[row][column] = "X"
        return board
    
    neighbors = get_neighbors(board, row, column)

    adjancent_mines_count = 0
    for neig_row, neig_col in neighbors:
        if board[neig_row][neig_col] == "M":
            adjancent_mines_count += 1
    
    if adjancent_mines_count:
        board[row][column] = str(adjancent_mines_count)
        return board
    
    board[row][column] = "0"
    for neig_row, neig_col in neighbors:
        if board[neig_row][neig_col] == "H":
            revealMinesweeper(board, neig_row, neig_col)
    
    return board

    


def get_neighbors(board, row, column):
    dirs = [-1, 0, 1]
    new_dirs = [
        (x, y)
        for y in dirs
        for x in dirs
        if not (x == 0 and y == 0)
    ]
    neighbors = []
    for delta_x, delta_y in new_dirs:
        new_row = row + delta_x
        new_col = column + delta_y
        if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]):
            neighbors.append((new_row, new_col))
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