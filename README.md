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
- When a `True` cell appears, that’s the start of an island.
- Explore everything connected to it using DFS (depth-first search).
- Mark visited cells so they aren’t counted twice.

### What is DFS (depth-first search)?

DFS explores in depth first — follow one path as far as it goes, then backtrack.

### Why iterative DFS?

Iterative DFS (depth-first search) uses a normal list as a stack.  
Recursion depends on the call stack, which has a finite depth.  
Large or deeply connected grids can exhaust it, so the iterative version is safer.

A recursive version is included as a reference.


## Python version

The utility was tested with **Python 3.12**, and this is the recommended version to use.
Other recent Python 3 versions should work as well, but 3.12 is the one this project was verified with.


## Installing Python (Windows 11)

1. Download from: https://www.python.org/downloads/windows/
2. During installation check: “Add Python to PATH”
3. Verify with: python --version


## Running the utility

python island_counter.py

Virtual environment (optional):
python -m venv .venv
.\.venv\Scripts\activate
python island_counter.py

## Running the tests

pip install pytest
pytest

## Notes
- The function modifies the grid in place.
- Pass a copy if you need to keep the original.
- Both DFS (depth-first search) versions work the same; the iterative one is safer for big grids.
