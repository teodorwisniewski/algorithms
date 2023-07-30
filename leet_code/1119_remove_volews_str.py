

class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        new_s = ""
        for ch in s:
            if ch not in vowels:
                new_s += ch
        return new_s
