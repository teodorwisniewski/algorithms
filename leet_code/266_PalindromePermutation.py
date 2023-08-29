from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = Counter(s)
        odd = 0
        for freq in counter.values():
            if freq % 2 != 0:
                odd += 1
                if odd > 1:
                    return False
        return True
            


sol = Solution()

s = "carerac"
res = sol.canPermutePalindrome(s)
assert res
