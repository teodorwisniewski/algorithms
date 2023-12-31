
from leetcode.sorting_merge_sort import merge


def test_merge_function():
    lst1 = [1, 2, 5]
    lst2 = [3, 4, 6]
    assert merge(lst1, lst2) == [1, 2, 3, 4, 5, 6]


def test_merge_empty():
    lst1 = [1, 2, 5]
    lst2 = []
    assert merge(lst1, lst2) == [1, 2, 5]


# sorting_fun = quick_sort_concise

# def test_sort_empty():
#     assert sorting_fun([]) == []


# def test_sort_single_element():
#     assert sorting_fun([1]) == [1]


# def test_sort_multiple_elements():
#     assert sorting_fun([3, 1, 2]) == [1, 2, 3]


# def test_sort_negative_elements():
#     assert sorting_fun([-1, -3, -2]) == [-3, -2, -1]


# def test_sort_mixed_elements():
#     assert sorting_fun([-1, 3, 0, 2, -5]) == [-5, -1, 0, 2, 3]