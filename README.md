# Island counter (8-connected)

Small Python utility for counting “islands” in a 2D boolean grid.  
An island is any group of one or more `True` cells that touch in any of the 8 directions
(horizontal, vertical, diagonal).

This came from a discussion during an interview — I said I'd take a closer look afterwards,
so I cleaned up the idea and wrote down both the iterative and recursive versions.

## Example

grid = [
    [False, True,  False, False],
    [False, True,  True,  False],
    [False, False, False, True ],
    [True,  False, False, True ],
]
# → 3

## How it works (quickly)

The idea is simple:
- Walk through the grid.
- When we hit a `True`, that’s the start of an island.
- Explore everything connected to it using DFS (depth-first search).
- Mark visited cells so they aren’t counted twice.

The main implementation uses iterative DFS (explicit stack) since Python’s recursion
limit can be hit on large or deep grids. A recursive version is included as reference.

## Run

    python island_counter.py

## Tests

    pip install pytest
    pytest

## Notes
- The function modifies the grid in place.
- Pass a copy if you need to keep the original.
