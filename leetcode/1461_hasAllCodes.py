
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) <= k:
            return False
        
        codes = set()
        for idx in range(len(s)-k+1):
            curr = s[idx:idx+k]
            codes.add(curr)

        return len(codes) == 2**k


sol = Solution()
# s = "00110110"
# k = 2
# res = sol.hasAllCodes(s, k)
# print(f"hasAllCodes {res}")


s = "00110"
k = 2
res = sol.hasAllCodes(s, k)
print(f"hasAllCodes {res}")
assert res