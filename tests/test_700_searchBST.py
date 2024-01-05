import pytest
from leetcode.problem_700_searchBST import Solution, TreeNode


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


@pytest.fixture
def bst():
    # Create a basic binary search tree
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    return root


def test_search_bst_found(bst):
    sol = Solution()
    node = sol.searchBST(bst, 2)
    assert node is not None
    assert node.val == 2


def test_search_bst_not_found(bst):
    sol = Solution()
    node = sol.searchBST(bst, 5)
    assert node is None
