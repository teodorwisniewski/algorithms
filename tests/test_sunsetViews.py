
from algo_expert.stacks.ex_3_sunsetViews import sunsetViews


def test_east_building():
    buildings = [3, 5, 4, 4, 3, 1, 3, 2]
    direction = "EAST"
    assert sunsetViews(buildings, direction) == [1, 3, 6, 7]

def test_west_building():
    buildings = [3, 5, 4, 4, 3, 1, 3, 2]
    direction = "WEST"
    assert sunsetViews(buildings, direction) == [0, 1]


