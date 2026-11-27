"""Count the islands in a grid map.

Land is '#', water is '.'. Two land cells are part of the same island
if they touch up, down, left or right (not diagonally).
"""

import sys
from collections import deque


def read_grid(path):
    with open(path) as f:
        return [line.rstrip("\n") for line in f if line.strip()]


def find_islands(grid):
    rows = len(grid)
    seen = set()
    islands = []

    for r in range(rows):
        for c in range(len(grid[r])):
            if grid[r][c] != "#" or (r, c) in seen:
                continue
            # flood fill from this cell
            cells = []
            queue = deque([(r, c)])
            seen.add((r, c))
            while queue:
                cr, cc = queue.popleft()
                cells.append((cr, cc))
                for nr, nc in ((cr - 1, cc), (cr + 1, cc), (cr, cc - 1), (cr, cc + 1)):
                    if 0 <= nr < rows and 0 <= nc < len(grid[nr]):
                        if grid[nr][nc] == "#" and (nr, nc) not in seen:
                            seen.add((nr, nc))
                            queue.append((nr, nc))
            islands.append(cells)
    return islands


def label_map(grid, islands):
    out = [list(row) for row in grid]
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i, cells in enumerate(islands):
        mark = letters[i % len(letters)]
        for r, c in cells:
            out[r][c] = mark
    return ["".join(row) for row in out]


def main():
    if len(sys.argv) != 2:
        print("usage: python islands.py MAPFILE")
        sys.exit(1)

    grid = read_grid(sys.argv[1])
    islands = find_islands(grid)

    print(f"Found {len(islands)} island(s)\n")
    for line in label_map(grid, islands):
        print(line)
    print()

    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i, cells in sorted(enumerate(islands), key=lambda x: -len(x[1])):
        print(f"  {letters[i % 26]}: {len(cells)} cells")


if __name__ == "__main__":
    main()
