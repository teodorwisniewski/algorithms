from typing import List


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s3) != len(s1) + len(s2):
            return False
        
        cache = [
            [None for _ in range(len(s2)+1)]
            for _ in range(len(s1)+1)
        ]
        return self.are_interwoven(s1, s2, s3, 0, 0, cache)
    
    def are_interwoven(self, s1: str, s2: str, s3: str, p1: int, p2: int,
                        cache: List[List]) -> bool:

        if cache[p1][p2] is not None:
            return cache[p1][p2]
        p3 = p1 + p2

        if p3 == len(s3):
            return True
        
        if p1 < len(s1) and s1[p1] == s3[p3]:
            cache[p1][p2] = self.are_interwoven(s1, s2, s3, p1+1, p2, cache)
            if cache[p1][p2]:
                return True
            
        if p2 < len(s2) and s2[p2] == s3[p3]:
            cache[p1][p2] = self.are_interwoven(s1, s2, s3, p1, p2+1, cache)
            return cache[p1][p2]
        
        cache[p1][p2] = False
        return cache[p1][p2]





sol = Solution()
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
res = sol.isInterleave(s1, s2, s3)
print(f"isInterleave {res}")