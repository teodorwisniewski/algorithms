
def nonAttackingQueens(n):

    used_cols = set()
    pos_diag = set()
    neg_diag = set()


    def backtrack(row_nb, acc=0):

        if row_nb == n:
            acc += 1
            return acc
        
        for col_nb in range(n):
            cond = (
                col_nb in used_cols or
                (row_nb + col_nb) in pos_diag or
                (row_nb - col_nb) in neg_diag
            )
            if cond:
                continue
            
            used_cols.add(col_nb)
            pos_diag.add(row_nb + col_nb)
            neg_diag.add(row_nb - col_nb)
            acc = backtrack(row_nb + 1, acc)
            used_cols.remove(col_nb)
            pos_diag.remove(row_nb + col_nb)
            neg_diag.remove(row_nb - col_nb)
        
        return acc
    
    return backtrack(0)

n = 4
res = nonAttackingQueens(n)
print(f"nonAttackingQueens {res}")