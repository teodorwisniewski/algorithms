
from leetcode.problem_75_sortColors import Solution


def test_sort_colors_example1():
    solution = Solution()
    nums = [2, 0, 2, 1, 1, 0]
    solution.sortColors(nums)
    assert nums == [0, 0, 1, 1, 2, 2]


def test_sort_colors_example2():
    solution = Solution()
    nums = [2, 0, 1]
    solution.sortColors(nums)
    assert nums == [0, 1, 2]


def test_sort_colors_empty():
    solution = Solution()
    nums = []
    solution.sortColors(nums)
    assert nums == []


def test_sort_colors_single_color():
    solution = Solution()
    nums = [1, 1, 1, 1]
    solution.sortColors(nums)
    assert nums == [1, 1, 1, 1]


def test_sort_colors_all_colors():
    solution = Solution()
    nums = [2, 2, 0, 0, 1, 1]
    solution.sortColors(nums)
    assert nums == [0, 0, 1, 1, 2, 2]
