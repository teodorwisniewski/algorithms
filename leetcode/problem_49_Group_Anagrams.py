from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        unique_anagrams = defaultdict(list)
        for anagram in strs:
            key = tuple(sorted(anagram))
            unique_anagrams[key].append(anagram)
        
        return unique_anagrams.values()





sol = Solution()

strs = ["eat","tea","tan","ate","nat","bat"]
res = sol.groupAnagrams(strs)
print(f"groupAnagrams {res}")

