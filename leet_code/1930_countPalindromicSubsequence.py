from collections import Counter
import string

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        right = Counter(s)
        left = set()
        res = set()
        lowercase_letters = string.ascii_lowercase

        for mid in range(len(s)):
            right[s[mid]] -= 1
            if not right[s[mid]]:
                right.pop(s[mid])
            
            for ch in lowercase_letters:
                if ch in left and ch in right:
                    res.add((s[mid], ch))
            left.add(s[mid])
        return len(res)


        



sol = Solution()
s = "aabca"
res = sol.countPalindromicSubsequence(s)
print(f"countPalindromicSubsequence {res}")