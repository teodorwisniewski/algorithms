

from leetcode.problem_509_fib import Solution 




def test_fib_base_cases():
    solution = Solution()
    assert solution.fib(0) == 0
    assert solution.fib(1) == 1


def test_fib_small():
    solution = Solution()
    assert solution.fib(5) == 5  # 5th Fibonacci number is 5
    assert solution.fib(6) == 8  # 6th Fibonacci number is 8


def test_fib_large():
    solution = Solution()
    # You can include a larger number if desired, but keep in mind the recursive implementation's performance
    assert solution.fib(10) == 55  # 10th Fibonacci number is 55

