from typing import List
from collections import Counter


# class Solution:
#     def totalFruit(self, fruits: List[int]) -> int:
#         left, right = 0, 0
#         counter = Counter()
#         res = 0
#         total = 0

#         for right in range(len(fruits)):
#             counter[fruits[right]] += 1
#             total += 1
#             while len(counter) > 2:
#                 given_left_fruit = fruits[left]
#                 counter[given_left_fruit] -= 1
#                 total -= 1
#                 left -= 1
#                 if counter[given_left_fruit] == 0:
#                     counter.pop(given_left_fruit)
#             res = max(res, total)
#         return res
        
class Solution:
    def totalFruit(self, fruits):
        counter = Counter()
        left = 0
        res = 0

        for right in range(len(fruits)):
            counter[fruits[right]] += 1
            while len(counter) > 2:
                counter[fruits[left]] -= 1
                if counter[fruits[left]] == 0:
                    del counter[fruits[left]]
                left += 1

            res = max(res, right - left + 1)

        return res



sol = Solution()
fruits = [0, 1, 2, 2]
res = sol.totalFruit(fruits)
print(f"totalFruit {res}")


fruits = [1,2,1]
res = sol.totalFruit(fruits)
print(f"totalFruit {res}")