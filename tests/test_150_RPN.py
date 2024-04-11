
import pytest

from leetcode.problem_150_evalRPN import Solution


@pytest.mark.parametrize("tokens, expected", [
    (["2","1","+","3","*"], 9),  # Test case 1
    (["4","13","5","/","+"], 6), # Test case 2
    (["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 22) # Test case 3       
])
def test_search(tokens, expected):
    sol = Solution()
    assert sol.evalRPN(tokens) == expected