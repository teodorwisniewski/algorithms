from collections import defaultdict
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board= board
        self.populate_existing_values()
        def backtrack(row_nb, col_nb):
            curr_row_idx = row_nb
            curr_col_idx = col_nb 
            if curr_col_idx == 9:
                curr_col_idx = 0
                curr_row_idx += 1
                if curr_row_idx == 9:
                    nonlocal is_solved
                    is_solved = True
                    return
            
            if board[curr_row_idx][curr_col_idx] != ".":
                backtrack(curr_row_idx, curr_col_idx+1)
            else:
                for num in range(1, 10):
                    if self.is_valid_candidate(num, curr_row_idx, curr_col_idx):
                        val = str(num)
                        self.row_values[curr_row_idx].add(val)
                        self.col_values[curr_col_idx].add(val)
                        box_id = curr_row_idx // 3 * 3 + curr_col_idx // 3
                        self.boxes_values[box_id].add(val)
                        board[curr_row_idx][curr_col_idx] = val
                        backtrack(curr_row_idx, curr_col_idx+1)
                        if not is_solved:
                            board[curr_row_idx][curr_col_idx] = "."
                            self.row_values[curr_row_idx].remove(val)
                            self.col_values[curr_col_idx].remove(val)
                            self.boxes_values[box_id].remove(val)


        is_solved = False 
        backtrack(0, 0)        
   
    def populate_existing_values(self):

        self.row_values = [set() for _ in range(9)]
        self.col_values = [set() for _ in range(9)]
        self.boxes_values = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = self.board[r][c]
                if val != ".":
                    self.row_values[r].add(val)
                    self.col_values[c].add(val)
                    box_id = r//3*3 + c//3
                    self.boxes_values[box_id].add(val)

    def is_valid_candidate(self, num, row_nb, col_nb):
        num = str(num)
        box_id = row_nb // 3 * 3 + col_nb // 3
        cond = (
            num not in self.board[row_nb] and
            num not in map(lambda board: board[col_nb], self.board) and
            num not in self.boxes_values[box_id]
        )
        return cond

   



sol = Solution()
board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]]



sol.solveSudoku(board)
print(f"solveSudoku {board}")