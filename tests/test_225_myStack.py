
from leetcode.problem_225_MyStack import MyStack 


def test_push_pop():
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.pop() == 1


def test_top():
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    assert stack.top() == 2


def test_empty():
    stack = MyStack()
    assert stack.empty()
    stack.push(1)
    assert not stack.empty()
    stack.pop()
    assert stack.empty()
