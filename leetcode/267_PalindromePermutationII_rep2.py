
from typing import List
from collections import Counter




class Solution:
    def generatePalindromes(self, s: str) -> List[str]:

        counter = Counter(s)
        odd_chars = [ch for ch, freq in counter.items() if freq % 2 != 0]
        
        if len(odd_chars) > 1:
            return []   
        elif odd_chars:
            odd_char = odd_chars[0]
            if counter[odd_char] == 1:
                del counter[odd_char]
            else:
                counter[odd_char] -= 1
        else:
            odd_char = ""

        results = []
        letters = [(letter, freq) for letter, freq in counter.items()]
        
        def backtrack(perm: str):

            if len(perm) == len(s):
                results.append(perm)
                return
            
            for i in range(len(letters)):
                letter, freq = letters[i]
                if not freq:
                    continue
                new_perm = letter + perm + letter
                letters[i] = (letter, freq-2)
                backtrack(new_perm)
                letters[i] = (letter, freq)
        
        backtrack(odd_char)
        return results

            




sol = Solution()

s = "aabb"
res = sol.generatePalindromes(s)
print(f"generatePalindromes {res}")

assert res


s = "acacbbc"
res = sol.generatePalindromes(s)
print(f"generatePalindromes {res}")