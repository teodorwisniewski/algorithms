from typing import List


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s3) != len(s1) + len(s2):
            return False
        
        dp = {}

        def backtrack(p1, p2) -> bool:

            if p1 == len(s1) and p2 == len(s2):
                return True
            
            if (p1, p2) in dp:
                return dp[p1, p2]
            
            p3 = p1 + p2

            if p1 < len(s1) and s1[p1] == s3[p3] and backtrack(p1+1, p2):
                return True
            
            if p2 < len(s2) and s2[p2] == s3[p3] and backtrack(p1, p2+1):
                return True

            dp[(p1, p2)] = False
            return False

        
        return backtrack(0, 0)


sol = Solution()
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
res = sol.isInterleave(s1, s2, s3)
print(f"isInterleave {res}")