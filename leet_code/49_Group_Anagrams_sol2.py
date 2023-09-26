from typing import List
from collections import Counter

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

#         unique_anagrams = defaultdict(list)
        
#         for word in strs:
#             word_key = [0] * 26
#             for ch in word:
#                 idx = ord(ch) - ord("a")
#                 word_key[idx] += 1
#             unique_anagrams[tuple(word_key)].append(word)
        
#         return unique_anagrams.values()



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        unique_anagrams = defaultdict(list)
        
        for word in strs:
            word_key = [0] * 26
            for ch in word:
                idx = ord(ch) - ord("a")
                word_key[idx] += 1
            unique_anagrams[tuple(word_key)].append(word)
        
        return unique_anagrams.values()




sol = Solution()

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
res = sol.groupAnagrams(strs)
print(f"groupAnagrams {res}")

