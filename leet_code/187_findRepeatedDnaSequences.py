from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen, res = set(), set()

        for left in range(len(s)-9):
            curr_subseq = s[left:left+10]
            if curr_subseq in seen:
                res.add(curr_subseq)
            else:
                seen.add(curr_subseq)
        return list(res)
                
        
sol = Solution()
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
res = sol.findRepeatedDnaSequences(s)
print(f"findRepeatedDnaSequences {res}")