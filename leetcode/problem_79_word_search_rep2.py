
from typing import List


# TC O(row*col*4^len(word)) SC(len(word))
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(row, col, idx):

            if idx == len(word):
                return True
            
            if (
                0 > row or row >= ROWS or
                0 > col or col >= COLS or
                (row, col) in path or
                word[idx] != board[row][col]
            ):
                return False
            
            path.add((row, col))
            res = (
                dfs(row+1, col, idx + 1) or
                dfs(row-1, col, idx + 1) or
                dfs(row, col+1, idx + 1) or
                dfs(row, col-1, idx + 1) 
            )
            path.remove((row, col))

            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
                


   

   
board = [
    list("SIEE"),
    list("SFMS"),
    list("ONAE")
]
word = "SIEMANO"

s = Solution()

# # Print the board
# for row in board:
#     print(' '.join(row))


# word = "SIEMANO"
# # Print the word
# print("Word:", word)
# print(f"word_exist {s.exist(board, word)}")

# word = "SIEMA"
# # Print the word
# print("Word:", word)
# print(f"word_exist {s.exist(board, word)}")

word = "SIEMU"
# Print the word
print("Word:", word)
print(f"word_exist {s.exist(board, word)}")