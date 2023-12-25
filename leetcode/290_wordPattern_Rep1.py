


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:


        
        words = s.split()

        if len(words) != len(pattern):
            return False

        words_to_chars = {}
        chars_to_words = {}

        for ch, word in zip(pattern, words):

            if (
                ch in chars_to_words and
                chars_to_words[ch] != word
            ):
                return False

            if (
                word in words_to_chars and
                words_to_chars[word] != ch
            ):
                return False     
            
            words_to_chars[word] = ch
            chars_to_words[ch] = word

        return True     
        




sol = Solution()

pattern = "abba"
s = "dog cat cat dog"
res = sol.wordPattern(pattern, s)
print(f'wordPattern {res}')


pattern = "abba"
s = "dog cat cat fish"
res = sol.wordPattern(pattern, s)
print(f'wordPattern {res}')