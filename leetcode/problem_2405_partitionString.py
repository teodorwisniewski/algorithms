

class Solution:
    def partitionString(self, s: str) -> int:
        curr_set = set()
        res = 1
        for ch in s:
            if ch in curr_set:
                res += 1
                curr_set = set()
            curr_set.add(ch)
        return res


sol = Solution()
s = "abacaba"
res = sol.partitionString(s)
print(f"partitionString {res}")