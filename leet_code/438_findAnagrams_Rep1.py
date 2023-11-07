from typing import List
from collections import Counter, defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(p) > len(s):
            return []
        
        sCount, pCount = {}, {}
        for idx in range(len(p)):
            sCount[s[idx]] = 1 + sCount.get(s[idx], 0)
            pCount[p[idx]] = 1 + pCount.get(p[idx], 0)

        res = [0] if sCount == pCount else []

        left = 0
        for right in range(len(p), len(s)):
            curr_ch = s[right]
            left_ch = s[left]
            sCount[curr_ch] = 1 + sCount.get(curr_ch, 0)
            sCount[left_ch] -= 1
            if not sCount[left_ch]:
                sCount.pop(left_ch)
            left += 1
            if sCount == pCount:
                res.append(left)
        return res

        

sol = Solution()
s = "cbaebabacd"
p = "abc"

res = sol.findAnagrams(s, p)
print(f"findAnagrams {res}")


s = "aa"
p = "bb"

res = sol.findAnagrams(s, p)
print(f"findAnagrams {res}")