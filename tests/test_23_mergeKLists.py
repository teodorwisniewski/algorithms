

import pytest
from leetcode.problem_23_mergeKLists import Solution, to_linked_list, to_list


@pytest.fixture
def solution():
    return Solution()


def test_merge_multiple_lists(solution):
    lists = [to_linked_list(l) for l in [[1, 4, 5], [1, 3, 4], [2, 6]]]
    assert to_list(solution.mergeKLists(lists)) == [1, 1, 2, 3, 4, 4, 5, 6]


def test_merge_empty_lists(solution):
    lists = []
    assert to_list(solution.mergeKLists(lists)) == []


def test_merge_lists_with_empty_list(solution):
    lists = [to_linked_list(l) for l in [[]]]
    assert to_list(solution.mergeKLists(lists)) == []
