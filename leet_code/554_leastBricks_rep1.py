from typing import List
from collections import defaultdict


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        gap_count = defaultdict(int)
        gap_count[0]

        for row in wall:
            total_len = 0
            for brick in row[:-1]:
                total_len += brick
                gap_count[total_len] += 1
        
        return len(wall) - max(gap_count.values())
    

sol = Solution()
wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
res = sol.leastBricks(wall)
print(f"leastBricks {res}")