
def nonAttackingQueens(n):

    blocked_cols = set()
    blocked_up_diag = set()
    blocked_down_diag = set()

    def is_valid_placement(row_nb, col_nb):

        if col_nb in blocked_cols:
            return False
        
        if row_nb + col_nb in blocked_up_diag:
            return False
        
        if row_nb - col_nb in blocked_down_diag:
            return False
        
        return True
    
    def place_queen(row_nb, col_nb):
        blocked_cols.add(col_nb)
        blocked_up_diag.add(row_nb + col_nb)
        blocked_down_diag.add(row_nb - col_nb)

    def remove_queen(row_nb, col_nb):
        blocked_cols.remove(col_nb)
        blocked_up_diag.remove(row_nb + col_nb)
        blocked_down_diag.remove(row_nb - col_nb)

    def backtrack(row_nb, acc=0):

        if row_nb == n:
            acc += 1
            return acc
        

        for col_nb in range(n):
            if is_valid_placement(row_nb, col_nb):
                place_queen(row_nb, col_nb)
                acc = backtrack(row_nb+1, acc)
                remove_queen(row_nb, col_nb)
        return acc
    
    return backtrack(0)


n = 4
res = nonAttackingQueens(n)
print(f"nonAttackingQueens {res}")