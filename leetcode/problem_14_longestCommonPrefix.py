from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]
        if len(strs) == 1:
            return first_word

        p = 0
        while p < len(first_word):
            current_letter = first_word[p]

            for word in strs:
                if p == len(word) or current_letter != word[p]:
                    return word[:p]
            p += 1
                    
        if p:
            return word[:p] 
 
        return ""





s = Solution()

# Print the word
strs = ["flower", "flow", "flight"]
strs = ["ab", "a"]
print(f"longestCommonPrefix {s.longestCommonPrefix(strs)}")