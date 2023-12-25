
from typing import List



class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stack = []
        for op in operations:

            if op == "D":
                last = stack[-1]
                new_score = 2 * int(last)
                stack.append(new_score)
            elif op == "+":
                last = int(stack[-1])
                second_to_last = stack[-2]
                new_score = last + second_to_last
                stack.append(new_score)            
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))

        return sum(stack)

        








sol = Solution()
ops = ["5","2","C","D","+"]
res = sol.calPoints(ops)
# "5" - Add 5 to the record, record is now [5].
# "2" - Add 2 to the record, record is now [5, 2].
# "C" - Invalidate and remove the previous score, record is now [5].
# "D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
# "+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
# The total sum is 5 + 10 + 15 = 30.
# Example 2:
assert res == 30
