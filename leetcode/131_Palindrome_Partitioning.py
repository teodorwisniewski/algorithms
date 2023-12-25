from typing import List


def is_palidrome(s):
    return s ==  s[::-1]

class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []

        def backtrack(part, idx):

            if idx >= len(s):
                res.append(part.copy())
                return

            for i in range(idx, len(s)):

                if is_palidrome(s[idx:i+1]):
                    part.append(s[idx:i+1])
                    backtrack(part, i+1)
                    part.pop()

                
               
                
        backtrack([], 0)
        return res







s = Solution()

res = s.partition("AAB")
print(f"partition {res}")