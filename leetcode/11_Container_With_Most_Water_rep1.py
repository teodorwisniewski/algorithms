
from typing import Optional, List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            left_height = height[left]
            right_height = height[right]
            width = right - left
            area = width * min(left_height, right_height)
            max_area = area if area > max_area else max_area
            if left_height < right_height:
                left += 1
            else:
                right -= 1
        return max_area
            



            
        

height = [1,8,6,2,5,4,8,3,7]

sol = Solution()
res = sol.maxArea(height)

print(f"maxArea {res}")