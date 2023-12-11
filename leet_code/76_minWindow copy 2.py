from collections import Counter



class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        left = 0
        counter_t, window = Counter(t), Counter()
        need, have = len(counter_t), 0
        resulting_idxs = [-1, -1]
        min_window_size = float("inf")

        for right, ch in enumerate(s):
            window[ch] += 1
            if window[ch] == counter_t[ch]:
                have += 1
            
            while have == need:
                new_window_size = right - left + 1
                if new_window_size < min_window_size:
                    min_window_size = new_window_size
                    resulting_idxs = [left, right]
                left_letter = s[left]
                window[left_letter] -= 1
                if left_letter in counter_t and window[left_letter] < counter_t[left_letter]:
                    have -= 1
                left += 1

        left, right = resulting_idxs
        return "" if resulting_idxs == float("inf") else s[left:right+1]
                

                





sol = Solution()
s = "ADOBECODEBANC"
t = "ABC"
res = sol.minWindow(s, t)
print(f"minWindow {res}")