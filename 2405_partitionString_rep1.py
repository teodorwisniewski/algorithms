

class Solution:
    def partitionString(self, s: str) -> int:
        partition = set()
        cnt = 1
        for ch in s:
            if ch in partition:
                partition = set()
                cnt += 1
            partition.add(ch)
        return cnt



sol = Solution()
s = "abacaba"
res = sol.partitionString(s)
print(f"partitionString {res}")