from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_len = len(s1)
        searched_perm = Counter(s1)
        sliding_window = Counter()

        for right in range(len(s2)):
            sliding_window[s2[right]] += 1
            if right >= window_len:
                left = right - window_len
                if sliding_window[s2[left]] == 1:
                    del sliding_window[s2[left]]
                else:
                    sliding_window[s2[left]] -= 1
   
            if searched_perm == sliding_window:
                return True
            
        return False
            
        
        


sol = Solution()
s1 = "ab"
s2 = "eidbaooo"
res = sol.checkInclusion(s1, s2)
print(f"checkInclusion {res}")
assert res