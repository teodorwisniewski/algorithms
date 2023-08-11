


# TC O(2n) SC (n)
class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = ['a', 'e', 'i', 'o', 'u']
        stack = []
        for ch in s:
            if ch.lower() in vowels:
                stack.append(ch)

        new_s = ''
        for ch in s:
            if ch.lower() in vowels:
                new_vowel = stack.pop()
                new_s += new_vowel
            else:
                new_s += ch
        return new_s