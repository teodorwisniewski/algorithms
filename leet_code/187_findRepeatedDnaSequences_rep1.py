from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        seen, res = set(), set()

        for idx in range(len(s)-9):
            curr = s[idx:idx+10]
            if curr in seen:
                res.add(curr)
            else:
                seen.add(curr)
        return res
    
        
sol = Solution()
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
res = sol.findRepeatedDnaSequences(s)
print(f"findRepeatedDnaSequences {res}")