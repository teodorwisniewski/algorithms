
from typing import List
from collections import Counter




class Solution:
    def generatePalindromes(self, s: str) -> List[str]:

        if not self.canPermutePalindrome(s):
            return []

        res = []

        def backtrack(perm):

            if len(s) == len(perm):
                res.append(perm)
                return
   
            for ch in list(self.counter.keys()):
                self.counter[ch] -= 2
                if not self.counter[ch]:
                    del self.counter[ch]
                new_perm = ch + perm + ch
                backtrack(new_perm)
                if ch not in self.counter:
                    self.counter[ch] = 2
                else:
                    self.counter[ch] += 2

        #  odd # of one letter
        if self.odd_letter:
            initial_perm = self.odd_letter
            self.counter[self.odd_letter] -= 1
            if not self.counter[self.odd_letter]:
                del self.counter[self.odd_letter]

            backtrack(initial_perm)
        else:
            backtrack("")

        return res

    def canPermutePalindrome(self, s: str) -> bool:
        counter = Counter(s)
        odd = 0
        self.odd_letter = None
        for val, freq in counter.items():
            if freq % 2 != 0:
                odd += 1
                self.odd_letter = val
                if odd > 1:
                    return False
        
        self.counter = counter
        return True



sol = Solution()

# s = "aabb"
# res = sol.generatePalindromes(s)
# print(f"generatePalindromes {res}")

# assert res


s = "acacbbc"
res = sol.generatePalindromes(s)
print(f"generatePalindromes {res}")