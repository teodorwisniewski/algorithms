from typing import List
from collections import defaultdict


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        count_gaps = defaultdict(int)
        count_gaps[0] = 0

        for row in wall:
            total_gap = 0
            for split in row[:-1]:
                total_gap += split
                count_gaps[total_gap] += 1
        
        return len(wall) - max(count_gaps.values())
    

sol = Solution()
wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
res = sol.leastBricks(wall)
print(f"leastBricks {res}")