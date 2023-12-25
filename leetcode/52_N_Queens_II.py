


class Solution:
    def totalNQueens(self, n: int) -> int:

        used_cols = set()
        used_pos_diag = set()
        used_neg_diag = set()

        def backtrack(row_nb=0, total=0):

            if row_nb == n:
                return total+1
            
            for col_nb in range(n):

                cond = (
                    col_nb in used_cols or
                    (row_nb + col_nb) in used_pos_diag or
                    (row_nb - col_nb) in used_neg_diag
                )
                if cond:
                    continue

                used_cols.add(col_nb)
                used_pos_diag.add(row_nb + col_nb)
                used_neg_diag.add(row_nb - col_nb)
                total = backtrack(row_nb+1, total)
                used_cols.remove(col_nb)
                used_pos_diag.remove(row_nb + col_nb)
                used_neg_diag.remove(row_nb - col_nb)

            return total                
            
        return backtrack()







s = Solution()
n = 4
res = s.totalNQueens(n)
print(f"totalNQueens {res}")
