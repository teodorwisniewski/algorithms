

from leetcode.stacks.problem_84_largestRectangleArea import Solution


def test_first_input():
    heights = [2, 1, 5, 6, 2, 3]
    sol = Solution()
    output = sol.largestRectangleArea(heights)
    assert output == 10


def test_second_input():
    heights = [2, 4]
    sol = Solution()
    output = sol.largestRectangleArea(heights)
    assert output == 4



def test_3_input():
    heights = [2,1,2]
    sol = Solution()
    output = sol.largestRectangleArea(heights)
    assert output == 3


    