
from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-el for el in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            biggest_stone = heapq.heappop(stones)
            second_biggest_stone = heapq.heappop(stones)
            crash = biggest_stone - second_biggest_stone
            if crash:
                heapq.heappush(stones, crash)
        if stones:
            return -stones[0]
        return 0



if __name__ == "__main__":

    sol = Solution()
    stones = [2,7,4,1,8,1]
    output = sol.lastStoneWeight(stones)
    assert output == 1