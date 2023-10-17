from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # hash mapping counting
        balloon_counter = Counter("balloon")
        text_counter = Counter(text)

        res = float("inf")
        for ch, freq in balloon_counter.items():
            res = min(res, text_counter[ch]//freq)
        return res




sol = Solution()
text = "loonbalxballpoon"
res = sol.maxNumberOfBalloons(text)
print(f"maxNumberOfBalloons {res}")