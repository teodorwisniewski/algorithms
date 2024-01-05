
from algo_expert.searching.algoexp_5_search_range_rep1 import searchForRange  

def test_multiple_occurrences():
    assert searchForRange([1, 3, 3, 5, 5, 5, 8, 9], 5) == [3, 5]

def test_single_occurrence():
    assert searchForRange([1, 2, 3, 4, 5, 6, 7, 8, 9], 4) == [3, 3]

def test_target_not_present():
    assert searchForRange([1, 2, 3, 4, 5, 6, 7, 8, 9], 10) == [-1, -1]

def test_empty_array():
    assert searchForRange([], 5) == [-1, -1]

def test_single_element_target():
    assert searchForRange([5], 5) == [0, 0]

def test_single_element_not_target():
    assert searchForRange([4], 5) == [-1, -1]

# Add more test cases if necessary
