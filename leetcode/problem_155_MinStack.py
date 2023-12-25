# import pdb


# class MinStack:

#     def __init__(self):
#         self.stack = []
#         self.correspoding_mins = []
#         self.min_el = float('inf')
    
#     def push(self, val: int) -> None:
#         self.stack.append(val)
#         if val < self.min_el:
#             self.min_el = val
#         self.correspoding_mins.append(self.min_el)
        
#     def pop(self) -> None:
#         if not self.stack:
#             return None
#         self.stack.pop()
#         self.correspoding_mins.pop()
#         if self.stack:
#             self.min_el = self.correspoding_mins[-1]
#         else:
#             self.min_el = float('inf')
        
#     def top(self) -> int:
#         if self.stack:
# #             return self.stack[-1]
        
        
#     def getMin(self) -> int:
#         if self.stack:
#             return self.min_el
    

class MinStack:

    def __init__(self):
        self.stack = []
        self.correspoding_mins = []
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.correspoding_mins and val > self.correspoding_mins[-1]:
            new_min = self.correspoding_mins[-1]
        else:
            new_min = val
        self.correspoding_mins.append(new_min)
        
    def pop(self) -> None:
        self.correspoding_mins.pop()
        self.stack.pop()
        
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        
    def getMin(self) -> int:
        if self.stack:
            return self.correspoding_mins[-1]
    