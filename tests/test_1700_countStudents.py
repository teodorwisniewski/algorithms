

from leetcode.problem_1700_countStudents import Solution 
def test_example_1():
    students = [1,1,0,0]
    sandwiches = [0,1,0,1]
    assert Solution().countStudents(students, sandwiches) == 0

def test_all_same_preference():
    students = [0, 0, 0, 0]
    sandwiches = [0, 0, 0, 0]
    assert Solution().countStudents(students, sandwiches) == 0

def test_no_matching_sandwiches():
    students = [1, 1, 1, 1]
    sandwiches = [0, 0, 0, 0]
    assert Solution().countStudents(students, sandwiches) == 4

def test_alternating_preferences():
    students = [1, 0, 1, 0]
    sandwiches = [0, 1, 0, 1]
    assert Solution().countStudents(students, sandwiches) == 0


def test_given_case():
    students = [1, 1, 1, 0, 0, 1]
    sandwiches = [1, 0, 0, 0, 1, 1]
    expected_output = 3
    assert Solution().countStudents(students, sandwiches) == expected_output

