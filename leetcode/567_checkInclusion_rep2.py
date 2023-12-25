class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_chars, s2_chars = [0] * 26, [0] * 26
        # create first window and desired window
        for i, ch in enumerate(s1):
            s1_chars[ord(ch)-ord('a')] += 1
            s2_chars[ord(s2[i])-ord('a')] += 1

        left = 0
        for right in range(len(s1), len(s2)):
            if s1_chars == s2_chars:
                return True
            
            # expand to right
            s2_chars[ord(s2[right])-ord('a')] += 1
            # shrink on the left
            s2_chars[ord(s2[left])-ord('a')] -= 1
            left += 1
            
        return s1_chars == s2_chars



sol = Solution()
s1 = "ab"
s2 = "eidbaooo"
res = sol.checkInclusion(s1, s2)
print(f"checkInclusion {res}")
assert res