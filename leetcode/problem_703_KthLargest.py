



class MinHeap:

    def __init__(self):
        self.heap = []

    def push(self, value: int):

        self.heap.append(value)
        self._percolate_up(len(self.heap)-1)
    
    def _parent_idx(self, idx:int) -> int:
        return (idx-1) // 2

    def _left_child_idx(self, idx: int) -> int:
        return (2 * idx + 1)

    def _right_child_idx(self, idx: int) -> int:
        return (2 * idx + 2)

    def _swap(self, idx1: int, idx2: int):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def _percolate_up(self, curr_idx: int): 
        
        parent_idx = self._parent_idx(idx)
        while (
            curr_idx > 0 and
            self.heap[curr_idx] < self.heap[parent_idx]
        ):
            self._swap(curr_idx, parent_idx)
            curr_idx = parent_idx
            parent_idx = self._parent_idx(curr_idx)
    
    def pop(self):

        if len(self.heap) == 0:
            return  
        
        if len(self.heap) == 1:
            return self.heap.pop()

        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._percolate_down(0)
        return min_value

    def _percolate_down(self, idx: int):

        left_child_idx = self._left_child_idx(idx)
        right_child_idx = self._right_child_idx(idx)

        while (
            left_child_idx < len(self.heap)  
        ):
            if (
                right_child_idx < len(self.heap) and
                self.heap[right_child_idx] < self.heap[left_child_idx] and
                self.heap[right_child_idx] < self.heap[idx]
            ):
                self._swap(right_child_idx, idx)
                idx = right_child_idx
            elif self.heap[left_child_idx] < self.heap[idx]:
                self._swap(left_child_idx, idx)
                idx = left_child_idx
            else:
                break








class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = MinHeap()
        for num in nums:
            self.min_heap.push(num)

        while len(self.min_heap.heap) > k:
            self.min_heap
        

    def add(self, val: int) -> int:
        




kthLargest = new KthLargest(3, [4, 5, 8, 2]);

kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8