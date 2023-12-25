from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def backtrack(stack: List, n_open: int, n_closed: int):

            if n_open == n_closed == n:
                res.append(''.join(stack))
                return
            
            if n_open < n:
                stack.append('(')
                backtrack(stack, n_open+1, n_closed)
                stack.pop()
            
            if n_open > n_closed:
                stack.append(')')
                backtrack(stack, n_open, n_closed+1)
                stack.pop()               

            
        res = []
        backtrack([], 0, 0)
        return res




s = Solution()


digits = 2
res = s.generateParenthesis(digits)
print(f"generateParenthesis {res}")

digits = 3
res = s.generateParenthesis(digits)
print(f"generateParenthesis {res}")
