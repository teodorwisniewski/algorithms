from collections import deque


class MyStack:

    def __init__(self):
        self.queue = []
        
    def push(self, x: int) -> None:
        # void push(int x) Pushes element x to the top of the stack.
        self.queue.append(x)

    def pop(self) -> int:
        # int pop() Removes the element on the top of the stack and returns it.
        return self.queue.pop()
        
    def top(self) -> int:
        # int top() Returns the element on the top of the stack.
        return self.queue[-1]
        
    def empty(self) -> bool:
        # boolean empty() Returns true if the stack is empty, false otherwise.
        return len(self.queue) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()