
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits) == 0:
            return []

        PHONE_MAPPING = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': '',
        }
        results = []

        def backtrack(idx, comb):

            if len(comb) == len(digits):
                results.append(''.join(comb))
                return
            if idx >= len(digits):
                return

            digit = digits[idx]
            possible_letters = list(PHONE_MAPPING[digit])
            for letter in possible_letters:
                comb.append(letter)
                backtrack(idx+1, comb)
                comb.pop()

        backtrack(0, [])
        return results
            

s = Solution()


digits = "23"
res = s.letterCombinations(digits)
print(f"letterCombinations {res}")

digits = ""
res = s.letterCombinations(digits)
print(f"letterCombinations {res}")
