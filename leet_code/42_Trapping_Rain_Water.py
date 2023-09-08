from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0 
        while left < right:

            if left_max <= right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]

        return water              







height = [0,1,0,2,1,0,1,3,2,1,2,1]

sol = Solution()
res = sol.trap(height)

print(f"trap {res}")