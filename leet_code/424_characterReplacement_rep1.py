
from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = Counter()
        left = 0
        max_length  = 0
        max_freq = 0

        for right in range(len(s)):
            counter[s[right]] += 1
            max_freq = max(max_freq, counter[s[right]])
            if (right - left + 1) - max_freq > k:
                counter[s[left]] -= 1
                left += 1
            max_length  = max(max_length , right - left + 1)
        return res

        


sol = Solution()
s = "AABABBA"
k = 1
res = sol.characterReplacement(s, k)
print(f"characterReplacement {res}")