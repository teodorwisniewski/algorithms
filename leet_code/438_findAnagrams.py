from typing import List
from collections import Counter, defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        sCount, pCount = defaultdict(int), Counter(p)

        for i in range(len(p)):
            sCount[s[i]] += 1
        
        res = [0] if pCount == sCount else []

        l = 0
        for r in range(len(p), len(s)):
            sCount[s[r]] += 1
            sCount[s[l]] -= 1
            if not sCount[s[l]]:
                sCount.pop(s[l])
            
            l += 1
            if sCount == pCount:
                res.append(l)
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