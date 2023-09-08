



# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = s.lower()
#         s = "".join([char for char in s if char.isalnum()])
#         return s == s[::-1]


# class Solution:
#     def isPalindrome(self, s: str) -> bool:
    
#         left, right = 0, len(s) - 1

#         while left < right:
#             if not self.is_alpha_nummeric(s[left]):
#                 left += 1
#             elif not self.is_alpha_nummeric(s[right]):
#                 right -= 1
#             elif s[left].lower() != s[right].lower():
#                 return False
#             else:
#                 left += 1
#                 right -= 1

#         return True
    
#     def is_alpha_nummeric(self, ch: str) -> bool:
#         cond = (
#             ord("A") <= ord(ch) <= ord("Z") or
#             ord("a") <= ord(ch) <= ord("z") or
#             ord("0") <= ord(ch) <= ord("9")
#         )
#         if cond:
#             return True
#         return False



input = "A man, a plan, a canal: Panama"
sol = Solution()
res = sol.isPalindrome(input)

print(f"isPalindrome {res}")

res = sol.isPalindrome("0P")

print(f"isPalindrome {res}")