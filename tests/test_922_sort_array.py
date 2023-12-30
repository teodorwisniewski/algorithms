
from leetcode.problem_922_sortArray_rep1 import Solution 


def test_sort_empty():
    assert Solution().sortArray([]) == []


def test_sort_single_element():
    assert Solution().sortArray([1]) == [1]


def test_sort_multiple_elements():
    assert Solution().sortArray([3, 1, 2]) == [1, 2, 3]


def test_sort_negative_elements():
    assert Solution().sortArray([-1, -3, -2]) == [-3, -2, -1]


def test_sort_mixed_elements():
    assert Solution().sortArray([-1, 3, 0, 2, -5]) == [-5, -1, 0, 2, 3]