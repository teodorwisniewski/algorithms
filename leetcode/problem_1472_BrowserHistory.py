


# class BrowserHistory:

#     __slots__ = ["current", "steps", "current_idx"]

#     def __init__(self, homepage: str):
#         self.current = homepage
#         self.current_idx = 0
#         self.steps = [homepage]

#     def visit(self, url: str) -> None:
#         # void visit(string url) Visits url from the current page. It clears up all the forward history.
#         if self.steps:
#             self.steps = self.steps[:self.current_idx+1]
#         self.current = url
#         self.steps.append(url)
#         self.current_idx += 1

#     def back(self, steps: int) -> str:
#         # string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x,
#         #  you will return only x steps. Return the current url after moving back in history at most steps.
#         if self.nb_of_history_steps == 1:
#             return self.current
#         if (new_idx := self.current_idx-steps) > 0:
#             self.current_idx = new_idx
#             self.current = self.steps[new_idx]
#         else:
#             self.current = self.steps[0]
#             self.current_idx = 0
#         return self.current
        
#     def forward(self, steps: int) -> str:
#         # string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x,
#         #  you will forward only x steps. Return the current url after forwarding in history at most steps.
#         self.current_idx = self.current_idx + steps
#         if self.nb_of_history_steps <= self.current_idx:
#             self.current_idx = self.nb_of_history_steps - 1

#         self.current = self.steps[self.current_idx]
#         return self.current
    
#     @property
#     def nb_of_history_steps(self):
#         return len(self.steps)
    
#     def current_page(self):
#         return self.current



class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class BrowserHistory:

    __slots__ = ["curr"]

    def __init__(self, homepage: str):
        self.curr = Node(homepage)
   
    def visit(self, url: str) -> None:
        # void visit(string url) Visits url from the current page. It clears up all the forward history.
        self.curr.next = Node(url, prev=self.curr)
        self.curr = self.curr.next


    def back(self, steps: int) -> str:
        # string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x,
        #  you will return only x steps. Return the current url after moving back in history at most steps.
        while self.curr.prev and steps > 0:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.value

    def forward(self, steps: int) -> str:
        # string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x,
        #  you will forward only x steps. Return the current url after forwarding in history at most steps.
        while self.curr.next and steps > 0:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.value

    def current_page(self):
        return self.curr.value


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)