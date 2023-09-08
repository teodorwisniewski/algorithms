
from typing import Optional, List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        res = 0
        left = 0
        right = len(height) - 1
        while left < right:
            left_val, right_val = height[left], height[right]
            area = (right - left) * min(left_val, right_val)
            res = max(res, area)

            if left_val < right_val:
                left += 1
            elif left_val > right_val:
                right -= 1
            else:
                left += 1
        return res
            
        

height = [1,8,6,2,5,4,8,3,7]

sol = Solution()
res = sol.maxArea(height)

print(f"maxArea {res}")