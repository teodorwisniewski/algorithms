
from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.s = s
        self.res = set()
        self.longest_str = -1
        self.backtrack(0, [], 0, 0)
        return self.res

    def backtrack(self, curr_idx: int, curr_res: List, left_count: int,
                  right_count: int):

        if curr_idx >= len(self.s):
            if left_count == right_count:
                if len(curr_res) > self.longest_str:
                    self.longest_str = len(curr_res)
                    self.res = set()
                    self.res.add("".join(curr_res))
                elif len(curr_res) == self.longest_str:
                    self.res.add("".join(curr_res))
        else:
            curr_ch = self.s[curr_idx]
            if curr_ch == "(":
                curr_res.append(curr_ch)
                self.backtrack(curr_idx+1, curr_res, left_count+1, right_count)
                curr_res.pop()
                # ignoring "(" parentesis
                self.backtrack(curr_idx+1, curr_res, left_count, right_count)
            elif curr_ch == ")":
                if left_count > right_count:
                    curr_res.append(curr_ch)
                    self.backtrack(curr_idx+1, curr_res, left_count, right_count+1)
                    curr_res.pop()
                # ignoring ")" parentesis
                self.backtrack(curr_idx+1, curr_res, left_count, right_count)
            else:
                curr_res.append(curr_ch)
                self.backtrack(curr_idx+1, curr_res, left_count, right_count)
                curr_res.pop()



sol = Solution()

s = "()())()"
res = sol.removeInvalidParentheses(s)
print(f"removeInvalidParentheses {res}")

s2 = ")(f"
res = sol.removeInvalidParentheses(s2)
print(f"removeInvalidParentheses {res}")

