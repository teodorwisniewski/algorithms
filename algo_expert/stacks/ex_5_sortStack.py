

def sortStack(stack):
    
    if not stack:
        return stack

    temp_value = stack.pop()
    sortStack(stack)

    insert_in_sorted_order(stack, temp_value)
    return stack

def insert_in_sorted_order(stack, value):
    if not stack or stack[-1] <= value:
        stack.append(value)
        return

    top_value = stack.pop()
    insert_in_sorted_order(stack, value)
    stack.append(top_value)



if __name__ == "__main__":
    stack = [2, 1, 2, 4, 3]
    expected_output = [1, 2, 2, 3, 4]
    output = sortStack(stack)
    print(f"sorted stack {output}")
    assert output == expected_output