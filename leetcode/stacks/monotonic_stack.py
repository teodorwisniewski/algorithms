
from typing import List

# From left to right monotonically decreasing 
# def get_next_greater_element(heights: List) -> List:

#     stack = []
#     results = [-1] * len(heights)
#     for idx, h in enumerate(heights):
#         while stack and stack[-1][1] < h:
#             top_idx, top_h = stack.pop()
#             results[top_idx] = h
#         stack.append((idx, h))
#         print(f"stack {stack}") 

#     return results


# From right to left monotonically decreasing 
def get_next_greater_element(heights: List) -> List:

    stack = []
    results = [-1] * len(heights)
    for idx in range(len(heights)-1, -1, -1):
        while stack and heights[idx] >= heights[stack[-1]]:
            stack.pop()

        if stack:    
            results[idx] = heights[stack[-1]]  
        stack.append(idx)
        print(f"stack {[heights[idx] for idx in stack]}") 

    return results


if __name__ == "__main__":
    heights = [2, 1, 2, 4, 3]
    expected_output = [4, 2, 4, -1, -1]
    output = get_next_greater_element(heights)
    print(output)
    assert output == expected_output