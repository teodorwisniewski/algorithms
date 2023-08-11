


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)

        result = ""
        p1 = 0
        p2 = 0
        while p1 < m or p2 < n:
            if p1 < m:
                result += word1[p1]
                p1 += 1
            if p2 < n:
                result += word2[p2] 
                p2 += 1
                
        return result
    

#     Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"