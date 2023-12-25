import pytest
from leetcode.problem_155_MinStack import MinStack


def test_push():
    stack = MinStack()
    stack.push(5)
    assert stack.top() == 5
    stack.push(3)
    assert stack.getMin() == 3
    stack.push(7)
    assert stack.top() == 7


def test_pop():
    stack = MinStack()
    stack.push(5)
    stack.push(3)
    stack.push(7)
    stack.pop()
    assert stack.top() == 3
    stack.pop()
    assert stack.getMin() == 5


def test_top():
    stack = MinStack()
    stack.push(5)
    assert stack.top() == 5


def test_get_min():
    stack = MinStack()
    stack.push(5)
    stack.push(3)
    assert stack.getMin() == 3
    stack.push(2)
    assert stack.getMin() == 2


def test_empty_stack():
    stack = MinStack()
    # with pytest.raises(IndexError):
    assert stack.top() is None
    # with pytest.raises(IndexError):
    assert stack.getMin() is None


def test_min_stack_operations():
    operations = ["MinStack", "push", "push", "push", "top", "pop", "getMin", "pop", "getMin", "pop", "push", "top", "getMin", "push", "top", "getMin", "pop", "getMin"]
    inputs = [[], [2147483646], [2147483646], [2147483647], [], [], [], [], [], [], [2147483647], [], [], [-2147483648], [], [], [], []]
    expected_outputs = [None, None, None, None, 2147483647, None, 2147483646, None, 2147483646, None, None, 2147483647, 2147483647, None, -2147483648, -2147483648, None, 2147483647]

    min_stack = None
    for op, value, expected in zip(operations, inputs, expected_outputs):
        if op == "MinStack":
            min_stack = MinStack()
        elif op == "push":
            min_stack.push(value[0])
        elif op == "pop":
            min_stack.pop()
        elif op == "top":
            top_val = min_stack.top()
            assert top_val == expected, f"Top value expected to be {expected}, got {top_val}"
        elif op == "getMin":
            min_val = min_stack.getMin()
            assert min_val == expected, f"Min value expected to be {expected}, got {min_val}"