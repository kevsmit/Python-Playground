from collections import deque
import sys

MAZE = [
    "##########",
    "#S.....#.#",
    "#.##.#.#.#",
    "#.#..#...#",
    "#.#.####.#",
    "#...#..#.#",
    "###.#.##.#",
    "#.....#..#",
    "#.###...E#",
    "##########",
]


def find(grid, ch):
    for r, row in enumerate(grid):
        c = row.find(ch)
        if c != -1:
            return r, c
    return None


def solve(grid):
    start = find(grid, "S")
    end = find(grid, "E")
    if start is None or end is None:
        return None

    came_from = {start: None}
    queue = deque([start])
    while queue:
        cur = queue.popleft()
        if cur == end:
            break
        r, c = cur
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[nr]):
                if grid[nr][nc] != "#" and (nr, nc) not in came_from:
                    came_from[(nr, nc)] = cur
                    queue.append((nr, nc))

    if end not in came_from:
        return None

    path = []
    step = end
    while step is not None:
        path.append(step)
        step = came_from[step]
    return path[::-1]


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            grid = [line.rstrip("\n") for line in f if line.strip()]
    else:
        grid = MAZE

    path = solve(grid)
    if path is None:
        print("No way out of this maze.")
        return

    rows = [list(row) for row in grid]
    for r, c in path[1:-1]:
        rows[r][c] = "*"
    for row in rows:
        print("".join(row))
    print(f"\nPath length: {len(path) - 1} steps")


if __name__ == "__main__":
    main()
