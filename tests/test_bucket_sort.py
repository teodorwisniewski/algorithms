
from leetcode.sorting_bucket_sort import bucket_sort


def test_standard_list():
    assert bucket_sort([1, 2, 2, 0, 0, 0]) == [0, 0, 0, 1, 2, 2]

def test_empty_list():
    assert bucket_sort([]) == []

def test_negative_numbers():
    assert bucket_sort([-3, -1, -2, -4, -5]) == [-5, -4, -3, -2, -1]

def test_with_duplicates():
    assert bucket_sort([3, 1, 2, 2, 4]) == [1, 2, 2, 3, 4]