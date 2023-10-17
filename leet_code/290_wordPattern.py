


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(words) != len(pattern):
            return False
        
        # checking one-to-one relationship
        words_to_char = {}
        char_to_words = {}
        for ch, word in zip(pattern, words):

            if word in words_to_char and words_to_char[word] != ch:
                return False
            
            if ch in char_to_words and char_to_words[ch] != word:
                return False

            words_to_char[word] = ch
            char_to_words[ch] = word

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