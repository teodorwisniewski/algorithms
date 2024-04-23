from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = [] # pair (idx, height)
        max_area = 0

        for curr_idx, curr_h in enumerate(heights):

            while stack and stack[-1][1] > curr_h:
                top_idx, top_h = stack.pop()
                if stack:
                    width = curr_idx - stack[-1][0] - 1
                else:
                    width = curr_idx
                area = top_h * width
                max_area = max(max_area, area)
            stack.append((curr_idx, curr_h))

        curr_idx += 1
        while stack:
            top_idx, top_h = stack.pop()
            if stack:
                width = curr_idx - stack[-1][0] - 1
            else:
                width = curr_idx
            area = top_h * width
            max_area = max(max_area, area)
        
        return max_area
