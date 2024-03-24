
import heapq
from typing import List

# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

#         distance_fun = lambda p: (p[0]*p[0]+ p[1]*p[1])
        
#         distances = [
#             (distance_fun(p), [p[0], p[1]])
#             for p in points
#         ]
#         # O(n)
#         heapq.heapify(distances)
#         print(distances)

#         return [
#             heapq.heappop(distances)[1]
#             for _ in range(k)
#         ]


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        
        for x, y in points:
            dist = - (x**2 + y**2)
            if len(heap) == k:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))

        return [
            [x, y]
            for (dist, x, y) in heap
        ]



if __name__ == "__main__":

    sol = Solution()
    points = [[3,3],[5,-1],[-2,4]]
    k = 2
    output = sol.kClosest(points, k)
    assert sorted([[3,3],[-2,4]]) == sorted(output)