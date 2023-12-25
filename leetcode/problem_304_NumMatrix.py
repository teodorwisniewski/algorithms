from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        ROWS, COLS = len(matrix), len(matrix[0])
        self.sum_mat = [
            [0] * (COLS + 1)
            for c in range(ROWS+1)
        ]
        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.sum_mat[r][c+1]
                self.sum_mat[r+1][c+1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
        bottom_right = self.sum_mat[row2][col2]
        above = self.sum_mat[row1-1][col2]
        left = self.sum_mat[row2][col1-1]
        top_left = self.sum_mat[row1-1][col1-1]
        return bottom_right - above - left + top_left
        




matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
num_matrix = NumMatrix(matrix)
res = num_matrix.sumRegion(2, 1, 4, 3)
assert res == 8
res = num_matrix.sumRegion(1, 1, 2, 2)
assert res == 11
res = num_matrix.sumRegion(1, 2, 2, 4)
assert res == 12