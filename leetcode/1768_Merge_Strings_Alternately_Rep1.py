

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        p1 = 0
        p2 = 0
        res = []
        while p1 < len(word1) and p2 < len(word2):

            res.append(word1[p1])
            res.append(word2[p2])
            p1 += 1
            p2 += 1
        
        res.append(word1[p1:])
        res.append(word2[p2:])
        return "".join(res)



            



sol = Solution()


word1 = "abc"
word2 = "pqr"
print(f"mergeAlternately { sol.mergeAlternately(word1, word2)}")