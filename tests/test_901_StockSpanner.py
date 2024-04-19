
from leetcode.problem_901_StockSpanner import StockSpanner


def test_stock_spanner():
    spanner = StockSpanner()
    # Test each next call and check its output
    assert spanner.next(100) == 1
    assert spanner.next(80) == 1
    assert spanner.next(60) == 1
    assert spanner.next(70) == 2
    assert spanner.next(60) == 1
    assert spanner.next(75) == 4
    assert spanner.next(85) == 6

def test_stock_spanner_with_repeating_prices():
    spanner = StockSpanner()
    assert spanner.next(50) == 1
    assert spanner.next(50) == 2
    assert spanner.next(50) == 3

def test_stock_spanner_with_increasing_prices():
    spanner = StockSpanner()
    assert spanner.next(30) == 1
    assert spanner.next(40) == 2
    assert spanner.next(50) == 3
    assert spanner.next(60) == 4

def test_stock_spanner_with_decreasing_prices():
    spanner = StockSpanner()
    results = [spanner.next(price) for price in [120, 110, 100, 90]]
    assert results == [1, 1, 1, 1]