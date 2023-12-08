from collections import Counter



class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        window, counter_t = Counter(), Counter(t)

        min_window_len = float("inf")
        res_left_right_idx = [-1, -1] # indexes for the resulting window
        have, need = 0, len(counter_t)
        left = 0
        for right, ch  in enumerate(s):
            window[ch] += 1
            if ch in counter_t and counter_t[ch] == window[ch]:
                have += 1
            
            while have == need:
                new_window_size = right - left + 1
                if new_window_size < min_window_len:
                    res_left_right_idx = [left, right]
                    min_window_len = new_window_size
                left_letter = s[left]
                window[left_letter] -= 1
                if left_letter in counter_t and window[left_letter] < counter_t[left_letter]:
                    have -= 1
                left += 1
        
        l, r = res_left_right_idx
        return "" if  res_left_right_idx == float("inf") else s[l:r+1]


                





sol = Solution()
s = "ADOBECODEBANC"
t = "ABC"
res = sol.minWindow(s, t)
print(f"minWindow {res}")