from data_structures.bst_bfs import MinHeap


def test_heap_initialization():
    heap = MinHeap()
    assert heap.heap == [], "Heap should be initialized empty"


def test_insert_single_element():
    heap = MinHeap()
    heap.insert(5)
    assert heap.heap == [5], "Heap should contain the single inserted element"


def test_insert_multiple_elements():
    heap = MinHeap()
    for value in [3, 1, 4, 1, 5, 9, 2, 6]:
        heap.insert(value)
    assert heap.heap[0] == min([3, 1, 4, 1, 5, 9, 2, 6]), "Root should be the smallest element"


def test_remove_min_element():
    heap = MinHeap()
    values = [5, 3, 8, 2, 10]
    for value in values:
        heap.insert(value)
    min_value = heap.remove()
    assert min_value == min(values), "Removed element should be the minimum"
    assert min_value not in heap.heap, "Removed element should no longer be in the heap"


def test_heap_property_after_multiple_operations():
    heap = MinHeap()
    values = [10, 4, 5, 30, 3, 20]
    for value in values:
        heap.insert(value)
    assert all(heap.heap[i] <= heap.heap[(i - 1) // 2] for i in range(1, len(heap.heap))), "Min-heap property violated after inserts"
    
    while heap.heap:
        prev_min = heap.remove()
        if heap.heap:
            assert prev_min <= heap.heap[0], "Min-heap property violated after removal"
