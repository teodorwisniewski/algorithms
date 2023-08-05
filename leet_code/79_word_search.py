
from typing import List


# TC O(row*col*4^len(word)) SC(len(word))
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        def dfs(row, col, word_idx, paths= None) -> bool:
            if paths is None:
                paths = set()
            # base cases
            if word_idx == len(word):
                return True
            false_cond = (
                row < 0 or
                col < 0 or
                row >= ROWS or
                col >= COLS or
                (row, col) in paths
            )
            if false_cond:
                return False
            
            # recursive case
            if word[word_idx] == board[row][col]:
                paths.add((row, col))
                res = (
                    dfs(row+1, col, word_idx+1, paths) or
                    dfs(row-1, col, word_idx+1, paths) or
                    dfs(row, col+1, word_idx+1, paths) or
                    dfs(row, col-1, word_idx+1, paths) 
                )
                paths.remove((row, col))
                return res
            return False
        
        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0):
                    return True
        return False


board = [
    list("SIEE"),
    list("SFMS"),
    list("ONAE")
]
word = "SIEMANO"

s = Solution()

# Print the board
for row in board:
    print(' '.join(row))


word = "SIEMANO"
# Print the word
print("Word:", word)
print(f"word_exist {s.exist(board, word)}")

word = "SIEMA"
# Print the word
print("Word:", word)
print(f"word_exist {s.exist(board, word)}")

word = "SIEMU"
# Print the word
print("Word:", word)
print(f"word_exist {s.exist(board, word)}")