

class MaxHeap:

    def __init__(self):
        self.heap = []

    def _parent_idx(self, idx):
        return (idx - 1) // 2
    
    def _swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def _left_child_idx(self, idx):
        return 2 * idx + 1
    
    def _right_child_idx(self, idx):
        return 2 * idx + 2
    
    def insert(self, value):
        self.heap.append(value)
        curr_idx = len(self.heap) - 1
        while (
            curr_idx > 0 and
            self.heap[curr_idx] > self.heap[self._parent_idx(curr_idx)]
        ):
            self._swap(curr_idx, self._parent_idx(curr_idx))
            curr_idx = self._parent_idx(curr_idx)
            
            



if __name__ == "__main__":

    h = MaxHeap()
    h.insert(99)
    h.insert(72)
    h.insert(61)
    h.insert(58)
    print(h.heap)
    assert [99, 72, 61, 58] == h.heap
    h.insert(100)
    print(h.heap)
    assert [100, 99, 61, 58, 72] == h.heap 



