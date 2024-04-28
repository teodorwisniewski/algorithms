
from collections import defaultdict


class FreqStack:

    def __init__(self):
        self. freq_to_vals_stacks = defaultdict(list)  # count: [numbers]
        self.max_cnt = 0
        self.nums_to_freq = {} # {}
        
    def push(self, val: int) -> None:
        val_count = 1 + self.nums_to_freq.get(val, 0)
        self.nums_to_freq[val] = val_count
        if val_count > self.max_cnt:
            self.max_cnt = val_count
        self.freq_to_vals_stacks[val_count].append(val)
        print(f"After adding {val} self. freq_to_vals_stacks={self. freq_to_vals_stacks}")
        print(f"After adding {val} self. nums_to_freq_stacks={self.nums_to_freq}")
        
    def pop(self) -> int:
        val_to_pop = self.freq_to_vals_stacks[self.max_cnt].pop()
        self.nums_to_freq[val_to_pop] -= 1
        if len(self.freq_to_vals_stacks[self.max_cnt]) == 0:
            self.max_cnt -= 1
        return val_to_pop

        




if __name__ == "__main__":


    freq_stack = FreqStack()
    for num in [5, 7, 5, 7, 4, 5]:
        freq_stack.push(num)
    

    assert 5 == freq_stack.pop()
    assert 7 == freq_stack.pop()
    assert 5 == freq_stack.pop()
    assert 4 == freq_stack.pop()
        