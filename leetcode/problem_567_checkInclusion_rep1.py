class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # Initialize character counts for s1 and for the first window of s2
        s1_count = [0] * 26
        s2_count = [0] * 26
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        # Slide the window and compare counts
        left = 0
        for right in range(len(s1), len(s2)):
            if s1_count == s2_count:
                return True
            # Add the new character to the count
            s2_count[ord(s2[right]) - ord('a')] += 1
            # Remove the oldest character from the count
            s2_count[ord(s2[left]) - ord('a')] -= 1
            left += 1

        # Check the last window
        return s1_count == s2_count


sol = Solution()
s1 = "ab"
s2 = "eidbaooo"
res = sol.checkInclusion(s1, s2)
print(f"checkInclusion {res}")
assert res