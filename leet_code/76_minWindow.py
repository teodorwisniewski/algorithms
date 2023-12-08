from collections import Counter



class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        count_t = Counter(t)
        window = Counter()

        left = 0
        res_len = float("inf")
        res = [-1, -1]
        have, need = 0, len(count_t)

        for right, ch in enumerate(s):
            window[ch] += 1
            if ch in count_t and window[ch] == count_t[ch]:
                have += 1
            while have == need:
                if (right-left+1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1
                l_ch = s[left]
                window[l_ch] -= 1
                if s[left] in count_t and window[s[left]] < count_t[s[left]]:
                    have -= 1
                left += 1
        
        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""



sol = Solution()
s = "ADOBECODEBANC"
t = "ABC"
res = sol.minWindow(s, t)
print(f"minWindow {res}")