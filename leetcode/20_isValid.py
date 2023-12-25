


class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        
        if len(s) % 2 == 1:
            return False
        
        
        left_brackets = ["{", "(", "["]
        right_brackets = ["}", ")", "]"]

        valid_brackets_mapping = {
            "{": "}", 
            "(": ")", 
            "[": "]"
        }
        stack = []

        for bracket in s:
            if bracket in left_brackets:
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                last_left_bracket = stack.pop()
                
                if valid_brackets_mapping[last_left_bracket] != bracket:
                    return False
        if len(stack) > 0:
            return False
        return True

sol = Solution()


s = "()[]{}"
res = sol.isValid(s)
assert res
s = "{()[]}"
res = sol.isValid(s)
assert res
s = "(]"
res = sol.isValid(s)
assert not res

s = "(("
res = sol.isValid(s)
assert not res

s = "){"
res = sol.isValid(s)
assert not res