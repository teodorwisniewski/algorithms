from typing import List
from collections import defaultdict


# class Solution:
#     def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:

#         for i in range(len(rectangles)):
#             rectangles[i] = rectangles[i][0]/rectangles[i][1]
#         hash_map = defaultdict(int)
#         for ratio in rectangles:
#             hash_map[ratio] += 1
#         res = 0
#         for value in hash_map.values():
#             res += value * (value-1)//2
#         return res


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:

        hash_map = defaultdict(int)
        for w, h in rectangles:
            hash_map[w/h] += 1
        res = 0
        for value in hash_map.values():
            res += value * (value-1)//2
        return res

        


sol = Solution()
rectangles = [
        [4, 8],
        [3, 6],
        [10, 20],
        [15, 30]
              ]
res = sol.interchangeableRectangles(rectangles)
print(f"interchangeableRectangles {res}")