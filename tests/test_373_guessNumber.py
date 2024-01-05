
import pytest
from leetcode.problem_373_guessNumber import Solution


# Mock the external guess API
def mock_guess(num, picked):
    return 0 if num == picked else -1 if num > picked else 1


def test_guess_number():
    solution = Solution()
    picked_number = 10

    # Monkey patch the external guess API
    solution.__class__.guess = lambda self, num: mock_guess(num, picked_number)
    
    assert solution.guessNumber(15) == picked_number


def test_guess_number_lower_bound():
    solution = Solution()
    picked_number = 1

    solution.__class__.guess = lambda self, num: mock_guess(num, picked_number)

    assert solution.guessNumber(5) == picked_number


def test_guess_number_upper_bound():
    solution = Solution()
    picked_number = 20

    solution.__class__.guess = lambda self, num: mock_guess(num, picked_number)

    assert solution.guessNumber(30) == picked_number