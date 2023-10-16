from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        count_characters = Counter(text)
        count_balloon = Counter("balloon")
        res = float("inf")
        for ch in count_balloon:
            res = min(res, count_characters[ch] // count_balloon[ch])
        return res
        




sol = Solution()
text = "loonbalxballpoon"
res = sol.maxNumberOfBalloons(text)
print(f"maxNumberOfBalloons {res}")