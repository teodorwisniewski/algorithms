
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:

        unique_codes = set()
        for idx in range(len(s)-k+1):
            code = s[idx:idx+k]
            unique_codes.add(code)
        
        return len(unique_codes) == 2**k
  
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