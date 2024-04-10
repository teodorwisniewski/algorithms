




class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        s = list(s)
        stack = []
        for idx, ch in enumerate(s):
            if ch == '(':
                stack.append(idx)
            elif ch == ')' and stack:
                stack.pop()
            elif ch == ')':
                s[idx] = ''


        for idx in stack:
            s[idx] = ''

            
        return ''.join(s)

        

    
        