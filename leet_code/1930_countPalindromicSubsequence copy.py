from collections import Counter
import string

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        lower_case = string.ascii_lowercase
        right = Counter(s)
        left = set()
        results = set()

        for idx in range(len(s)):
            right[s[idx]] -= 1
            if right[s[idx]] == 0:
                right.pop(s[idx])
            for ch in lower_case:
                if ch in left and ch in right:
                    results.add((s[idx], ch))
            left.add(s[idx])
        return len(results)


        



sol = Solution()
s = "aabca"
res = sol.countPalindromicSubsequence(s)
print(f"countPalindromicSubsequence {res}")