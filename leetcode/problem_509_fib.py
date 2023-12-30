


class Solution:
    def fib(self, n: int) -> int:

        if n <= 1:
            return n
        prev = 0
        nxt = 1
        i = 0 
        while i < (n-1):
            nxt, prev = nxt + prev, nxt
            i += 1

        return nxt