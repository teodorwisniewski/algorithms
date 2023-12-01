
from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_len = 0
        counter = Counter()
        max_cnt = 0
        for right in range(len(s)):
            counter[s[right]] += 1
            max_cnt = max(max_cnt, counter[s[right]])
            while ((right - left + 1) - max_cnt) > k:
                counter[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len

        


sol = Solution()
s = "AABABBA"
k = 1
res = sol.characterReplacement(s, k)
print(f"characterReplacement {res}")