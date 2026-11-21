import sys

# 0 means empty
PUZZLE = """
530070000
600195000
098000060
800060003
400803001
700020006
060000280
000419005
000080079
"""


def read_grid(text):
    rows = [line.strip() for line in text.strip().splitlines() if line.strip()]
    grid = [[int(ch) for ch in row.replace(".", "0")] for row in rows]
    if len(grid) != 9 or any(len(r) != 9 for r in grid):
        raise ValueError("need 9 rows of 9 digits")
    return grid


def can_place(grid, r, c, n):
    if n in grid[r]:
        return False
    if any(grid[i][c] == n for i in range(9)):
        return False
    br, bc = 3 * (r // 3), 3 * (c // 3)
    for i in range(br, br + 3):
        for j in range(bc, bc + 3):
            if grid[i][j] == n:
                return False
    return True


def solve(grid):
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                for n in range(1, 10):
                    if can_place(grid, r, c, n):
                        grid[r][c] = n
                        if solve(grid):
                            return True
                        grid[r][c] = 0
                return False
    return True


def show(grid):
    for r in range(9):
        if r % 3 == 0 and r:
            print("------+-------+------")
        parts = []
        for c in range(9):
            if c % 3 == 0 and c:
                parts.append("|")
            parts.append(str(grid[r][c]) if grid[r][c] else ".")
        print(" ".join(parts))


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            grid = read_grid(f.read())
    else:
        grid = read_grid(PUZZLE)

    print("Puzzle:")
    show(grid)
    print()
    if solve(grid):
        print("Solved:")
        show(grid)
    else:
        print("No solution found.")


if __name__ == "__main__":
    main()
