from typing import List

NEIGHBOUR_OFFSETS = [
    (dr, dc)
    for dr in (-1, 0, 1)
    for dc in (-1, 0, 1)
    if not (dr == 0 and dc == 0)
]

def count_islands(grid: List[List[bool]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])

    def flood(start_r: int, start_c: int) -> None:
        stack = [(start_r, start_c)]
        grid[start_r][start_c] = False

        while stack:
            r, c = stack.pop()
            for dr, dc in NEIGHBOUR_OFFSETS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc]:
                    grid[nr][nc] = False
                    stack.append((nr, nc))

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c]:
                count += 1
                flood(r, c)

    return count

def count_islands_recursive(grid: List[List[bool]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])

    def dfs(r: int, c: int) -> None:
        grid[r][c] = False
        for dr, dc in NEIGHBOUR_OFFSETS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc]:
                dfs(nr, nc)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c]:
                count += 1
                dfs(r, c)

    return count

if __name__ == "__main__":
    example_grid = [
        [False, True,  False, False],
        [False, True,  True,  False],
        [False, False, False, True ],
        [True,  False, False, True ],
    ]

    print("Input grid:")
    for row in example_grid:
        print(row)

    result = count_islands(example_grid)
    print("\nIslands found (iterative DFS):", result)
