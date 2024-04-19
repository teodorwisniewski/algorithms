
from leetcode.problem_71_simplifyPath import Solution


def test_simplifyPath_example1():
    solution = Solution()
    input = "/home/"
    output = solution.simplifyPath(input)
    assert output == "/home"


def test_simplifyPath_example2():
    solution = Solution()
    input = "/../"
    output = solution.simplifyPath(input)
    assert output == "/"


def test_simplifyPath_example3():
    solution = Solution()
    input = "/home//foo/"
    output = solution.simplifyPath(input)
    assert output == "/home/foo"


def test_simplifyPath_example4():
    solution = Solution()
    input = "/a/../../b/../c//.//"
    output = solution.simplifyPath(input)
    assert output == "/c"
    