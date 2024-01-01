
from leetcode.sorting_quick_sort import quick_sort, quick_sort_concise


sorting_fun = quick_sort

def test_sort_empty():
    assert sorting_fun([]) == []


def test_sort_single_element():
    assert sorting_fun([1]) == [1]


def test_sort_multiple_elements():
    assert sorting_fun([3, 1, 2]) == [1, 2, 3]


def test_sort_negative_elements():
    assert sorting_fun([-1, -3, -2]) == [-3, -2, -1]


def test_sort_mixed_elements():
    assert sorting_fun([-1, 3, 0, 2, -5]) == [-5, -1, 0, 2, 3]


def test_repeated_values_elements():
    assert sorting_fun([1, 2, 3, 3, 3, 1, 0, 7]) == [0, 1, 1, 2, 3, 3, 3, 7]
