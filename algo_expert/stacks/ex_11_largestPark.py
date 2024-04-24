


def largestPark(land) -> int:
    
    heights = [0] * len(land[0])
    max_area = 0
    for row_idx, row in enumerate(land):
        for col_idx in range(len(land[0])):
            heights[col_idx] = heights[col_idx] + 1 if row[col_idx] is False else 0
        max_area = max(max_area, get_max_rectagle_from_histogram(heights))
        print(f'row: {row_idx} and heights;: {heights}')
    
    return max_area

def get_max_rectagle_from_histogram(heights) -> int:

    stack = []
    max_rec = 0
    for idx, curr_h in enumerate(heights):

        while stack and stack[-1][1] > curr_h:
            top_idx, top_h = stack.pop()
            width = idx if not stack else idx - stack[-1][0] - 1
            area = top_h * width
            max_rec = max(max_rec, area)
        stack.append((idx, curr_h))
    
    idx += 1
    while stack:
        top_idx, top_h = stack.pop()
        width = idx if not stack else idx - stack[-1][0] - 1
        area = top_h * width
        max_rec = max(max_rec, area)

    return max_rec



if __name__ == "__main__":
    # land = [
    #     [False, True, True, True, False],
    #     [False, False, False, True, False],
    #     [False, False, False, False, False],
    #     [False, True, True, True, True]
    # ]
    # expected_output = 6
    # output = largestPark(land)
    # print(f"largestPark {output}")
    # assert output == expected_output

    land = [
        [True, True, False, True, False],
        [False, True, False, False, False],
        [True, False, False, False, False],
        [False, True, True, False, True]
    ]
    expected_output = 6
    output = largestPark(land)
    print(f"largestPark {output}")
    assert output == expected_output