

def replace_char_at_index(input_str, index, char):
    return input_str[:index] + char + input_str[index+1:]


def is_palidrome(s):
    return s == s[::-1]


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n < 2:
            return ""

        for i in range(0, n//2):
            if palindrome[i] != "a":
                return replace_char_at_index(palindrome, i, "a")
        
        new_palidrome = replace_char_at_index(palindrome, n-1, "b")

        return new_palidrome
    
        
s = Solution()
palindrome = "abccba"
res = s.breakPalindrome(palindrome)
print(f"breakPalindrome {res}")


s = Solution()
palindrome = "aa"
res = s.breakPalindrome(palindrome)
print(f"breakPalindrome {res}")



palindrome2 = "a"
res2 = s.breakPalindrome(palindrome2)
print(f"breakPalindrome {res2}")