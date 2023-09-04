from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transposed_matrix = []
        w = len(matrix[0])
        h = len(matrix)
        for row_nb in range(w):
            new_row = []
            for col_nb in range(h):
                new_row.append(matrix[col_nb][row_nb])
            transposed_matrix.append(new_row)
        return transposed_matrix






matrix = [
  [1, 2],
  [3, 4],
  [5, 6]
]

sol = Solution()
res = sol.transpose(matrix)
print(f"transpose {res}")