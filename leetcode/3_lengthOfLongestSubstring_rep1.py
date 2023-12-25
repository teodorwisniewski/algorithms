


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         char_set = set()
#         left = 0
#         longest_sub = 0
#         for right in range(len(s)):
#             while s[right] in char_set:
#                 char_set.remove(s[left])
#                 left += 1
#             char_set.add(s[right])
#             longest_sub = max(longest_sub, right - left + 1)
#         return longest_sub


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = dict() # letter to index
        left = 0
        longest_sub = 0
        for right, ch in enumerate(s):
            if ch in char_map:
                left = max(left, char_map[ch] + 1)
            char_map[ch] = right
            longest_sub = max(longest_sub, right - left + 1)
        return longest_sub


sol = Solution()
# s = "pwwkew"
# res = sol.lengthOfLongestSubstring(s)
# print(f"lengthOfLongestSubstring {res}")

s = "abba"
res = sol.lengthOfLongestSubstring(s)
print(f"lengthOfLongestSubstring {res}")
assert res == 2