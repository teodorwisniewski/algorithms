
import operator
from typing import List


def division_towards_zero(a, b):
    return int(a/b)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': division_towards_zero
        }
        stack = []
        for token in tokens:
            if oper := operations.get(token):
                a, b = stack.pop(), stack.pop()
                stack.append(oper(b, a))
            else:
                stack.append(int(token))
        return stack[0]
        
        