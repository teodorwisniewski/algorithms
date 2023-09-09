


class Solution:
    def validPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1

        while left < right:

            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                if (
                    self.helper_is_palidrome(s[left:right]) or
                    self.helper_is_palidrome(s[left+1:right+1])
                ):
                    return True
                return False
                
        return True

    def helper_is_palidrome(self, s):
        left = 0
        right = len(s) - 1

        while left < right:

            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
        



sol = Solution()


s = "abca"
res = sol.validPalindrome(s)
print(f"validPalindrome {res}")

s = "abc"
res = sol.validPalindrome(s)
print(f"validPalindrome {res}")


