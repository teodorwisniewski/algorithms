
import pytest
from leetcode.problem_704_binary_search import Solution


@pytest.mark.parametrize("nums, target, expected", [
    ([-1,0,3,5,9,12], 9, 4),  # Test case 1
    ([-1,0,3,5,9,12], 2, -1), # Test case 2
    ([], 1, -1),              # Test case 3: Empty list
    ([1], 1, 0),              # Test case 4: Single element list
    ([1, 2, 3, 4, 5], 3, 2),  # Test case 5: Multiple elements
])
def test_search(nums, target, expected):
    sol = Solution()
    assert sol.search(nums, target) == expected