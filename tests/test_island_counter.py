import copy
from island_counter import count_islands

def clone(grid):
    return copy.deepcopy(grid)

def test_small_diagonal():
    grid = clone([
        [True, False],
        [False, True],
    ])
    assert count_islands(grid) == 1
