

from typing import List

# def sort_stack(stack: List) -> List:

#     additional_stack = []
#     while stack:
#         temp_value = stack.pop()
#         while additional_stack and additional_stack[-1] < temp_value:
#             stack.append(additional_stack.pop())
#         additional_stack.append(temp_value)

#     while additional_stack:
#         stack.append(additional_stack.pop())

#     return stack


def sort_stack(stack: List) -> List:

    additional_stack = []

    while stack:
        additional_stack.append(stack.pop())
    
    while additional_stack:

        # correct order for inserting
        # no swapping needed
        # or empty stack
        if not stack or stack[-1] <= additional_stack[-1]:
            stack.append(additional_stack.pop())
        
        else:
            # insert and sort remaining stack
            # incorrect order
            # The additional_stack has a value that is smaller
            # then the top of the target stack
            # we need to insert the top of the additional stack
            # at the correct position into a stack
            additional_s_top = additional_stack.pop()
            while stack and stack[-1] > additional_s_top:
                additional_stack.append(stack.pop())
            
            # once all bigger values than add_temp_value from the stsack
            # have been removed. We may insert add_temp_value into the stack
            stack.append(additional_s_top)
    return stack

    


if __name__ == "__main__":
    heights = [2, 1, 2, 4, 3]
    expected_output = [1, 2, 2, 3, 4]
    output = sort_stack(heights)
    print(f"sorted stack {output}")
    assert output == expected_output