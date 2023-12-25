import pytest
from leetcode.155_MinStack import MinStack


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
    with pytest.raises(IndexError):
        _ = stack.top()
    with pytest.raises(IndexError):
        _ = stack.getMin()

# Additional tests can be added to cover more scenarios.
