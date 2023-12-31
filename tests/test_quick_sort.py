
from leetcode.sorting_quick_sort import quick_sort


def test_sort_empty():
    assert quick_sort([]) == []


def test_sort_single_element():
    assert quick_sort([1]) == [1]


def test_sort_multiple_elements():
    assert quick_sort([3, 1, 2]) == [1, 2, 3]


def test_sort_negative_elements():
    assert quick_sort([-1, -3, -2]) == [-3, -2, -1]


def test_sort_mixed_elements():
    assert quick_sort([-1, 3, 0, 2, -5]) == [-5, -1, 0, 2, 3]