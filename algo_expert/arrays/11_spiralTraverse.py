

def spiralTraverse(array):

    start_row, end_row = 0, len(array) - 1
    start_col, end_col = 0, len(array[0]) - 1
    result = []

    def spiral_fill(start_row, end_row, start_col, end_col):

        if start_row > end_row or start_col > end_col:
            return
        
        # upper bound
        for col in range(start_col, end_col+1):
            result.append(array[start_row][col])

        # right bound
        for row in range(start_row+1, end_row+1):
            result.append(array[row][end_col])

        # bottom bound
        for col in reversed(range(start_col, end_col)):
            if start_row == end_row:
                break
            result.append(array[end_row][col])

        # left bound
        for row in reversed(range(start_row+1, end_row)):
            if start_col == end_col:
                break
            result.append(array[row][start_col])

        spiral_fill(start_row+1, end_row-1, start_col+1, end_col-1)
    
    spiral_fill(start_row, end_row, start_col, end_col)
    return result


array = [
  [1,   2,  3, 4],
  [12, 13, 14, 5],
  [11, 16, 15, 6],
  [10,  9,  8, 7],
]


res = spiralTraverse(array)

print(f'spiralTraverse {res}')


arr2 = [
    [1, 2, 3, 4],
    [10, 11, 12, 5],
    [9, 8, 7, 6]
  ]

res = spiralTraverse(arr2)

print(f'spiralTraverse {res}')