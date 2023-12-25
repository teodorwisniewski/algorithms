import random
# class RandomizedSet:

#     def __init__(self):
#         self.values = list()
#         self.val_set = set()

        

#     def insert(self, val: int) -> bool:
#         if val not in self.val_set:
#             self.values.append(val)
#             self.val_set.add(val)
#             return True
#         return False
        

#     def remove(self, val: int) -> bool:
#         if val in self.val_set:
#             self.values.remove(val)
#             self.val_set.remove(val)
#             return True
#         return False
        
#     def getRandom(self) -> int:
#         if self.values:
#             random_idx = randint(0, len(self.values)-1)
#             return self.values[random_idx]


class RandomizedSet:

    def __init__(self):
        self.nums_list = list()
        self.nums_map = dict()

    def insert(self, val: int) -> bool:
        res = val not in self.nums_map
        if res:
            self.nums_map[val] = len(self.nums_list)
            self.nums_list.append(val)
        return res

    def remove(self, val: int) -> bool:
        res = val in self.nums_map
        if res:
            idx = self.nums_map[val]
            last_val = self.nums_list[-1]
            self.nums_list[idx] = last_val
            self.nums_list.pop()
            self.nums_map[last_val] = idx
            del self.nums_map[val]
        return res
        
    def getRandom(self) -> int:
        return random.choice(self.nums_list)


obj = RandomizedSet()
print(obj.insert(3))
print(obj.remove(3))
print(obj.remove(3))
print(obj.insert(4))
print(obj.insert(4))
print(obj.insert(5))
print(obj.insert(6))
print(obj.getRandom())
print(obj.getRandom())