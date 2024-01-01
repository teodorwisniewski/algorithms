

import pytest
from leetcode.problem_21_merged_sorted_list_rep1 import Solution, to_linked_list, to_list  # assuming your Solution class is in a file named solution.py

@pytest.fixture
def solution():
    return Solution()


def test_merge_two_non_empty_lists(solution):
    list1 = to_linked_list([1, 2, 4])
    list2 = to_linked_list([1, 3, 4])
    merged = solution.mergeTwoLists(list1, list2)
    assert to_list(merged) == [1, 1, 2, 3, 4, 4]

def test_merge_two_empty_lists(solution):
    list1 = to_linked_list([])
    list2 = to_linked_list([])
    merged = solution.mergeTwoLists(list1, list2)
    assert to_list(merged) == []

def test_merge_empty_and_non_empty_list(solution):
    list1 = to_linked_list([])
    list2 = to_linked_list([0])
    merged = solution.mergeTwoLists(list1, list2)
    assert to_list(merged) == [0]


