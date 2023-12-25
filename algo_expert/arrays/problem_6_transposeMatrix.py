


#  TC O(wxh) SC O(wxh)
def transposeMatrix(matrix):
    nb_rows = len(matrix)
    nb_columns = len(matrix[0])
    new_matrix = [] 

    for row_nb in range(nb_columns):
        new_row = []
        for col_nb in range(nb_rows):
            val = matrix[col_nb][row_nb]
            new_row.append(val)
        new_matrix.append(new_row)

    return new_matrix



matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

res = transposeMatrix(matrix)
print(f"nonConstructibleChange {res}")

