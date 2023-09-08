



class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join([char for char in s if char.isalnum()])
        return s == s[::-1]


input = "A man, a plan, a canal: Panama"
sol = Solution()
res = sol.isPalindrome(input)

print(f"isPalindrome {res}")

res = sol.isPalindrome("0P")

print(f"isPalindrome {res}")