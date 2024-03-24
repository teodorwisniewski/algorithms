
import heapq
from typing import List

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
        
#         heap = []
#         for el in nums:

#             if len(heap) == k:
#                 heapq.heappushpop(heap, el)
#             else:
#                 heapq.heappush(heap, el)

#         return heap[0]

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = [-num for num in nums]
        heapq.heapify(heap)

        for _ in range(k-1):
            heapq.heappop(heap)

        return -heapq.heappop(heap)

if __name__ == "__main__":

    sol = Solution()
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    output = sol.findKthLargest(nums, k)
    assert 4 == output