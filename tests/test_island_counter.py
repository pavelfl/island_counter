import copy
from island_counter import count_islands

def clone(g):
    return copy.deepcopy(g)

def test_simple():
    grid = clone([
        [True, False],
        [False, True],
    ])
    assert count_islands(grid) == 1
