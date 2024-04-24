

from typing import List

# From left to right monotonically decreasing 
def sort_stack(stack: List) -> List:

    additional_stack = []
    while stack:
        temp_value = stack.pop()
        while additional_stack and additional_stack[-1] < temp_value:
            stack.append(additional_stack.pop())
        additional_stack.append(temp_value)

    while additional_stack:
        stack.append(additional_stack.pop())

    return stack


if __name__ == "__main__":
    heights = [2, 1, 2, 4, 3]
    expected_output = [1, 2, 2, 3, 4]
    output = sort_stack(heights)
    print(f"sorted stack {output}")
    assert output == expected_output