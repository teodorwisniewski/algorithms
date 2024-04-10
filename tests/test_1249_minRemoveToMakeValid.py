

import pytest

from leetcode.problem_1249_minRemoveToMakeValid import Solution


def test_normal_case():
    sol = Solution()
    assert sol.minRemoveToMakeValid('a)bs(d)') == 'abs(d)'


def test_normal_case_two_possible():
    sol = Solution()
    assert sol.minRemoveToMakeValid('(abs(d)e') in ['abs(d)e', '(absd)e']


def test_normal_case_empty_str_response():
    sol = Solution()
    assert sol.minRemoveToMakeValid('))((') == ''