import sys
import time
import random


def make_grid(rows, cols, fill=0.3):
    return [[1 if random.random() < fill else 0 for _ in range(cols)] for _ in range(rows)]


def count_neighbors(grid, r, c):
    rows = len(grid)
    cols = len(grid[0])
    total = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            # wrap around the edges
            total += grid[(r + dr) % rows][(c + dc) % cols]
    return total


def step(grid):
    new = []
    for r in range(len(grid)):
        row = []
        for c in range(len(grid[0])):
            n = count_neighbors(grid, r, c)
            if grid[r][c] == 1:
                row.append(1 if n in (2, 3) else 0)
            else:
                row.append(1 if n == 3 else 0)
        new.append(row)
    return new


def show(grid, gen):
    print("\033[H\033[J", end="")  # clear screen
    print("generation", gen)
    for row in grid:
        print("".join("#" if cell else "." for cell in row))


def main():
    gens = 50
    if len(sys.argv) > 1:
        gens = int(sys.argv[1])

    grid = make_grid(20, 40)
    for gen in range(gens):
        show(grid, gen)
        new = step(grid)
        if new == grid:
            print("nothing changing anymore, stopping")
            break
        grid = new
        time.sleep(0.15)


if __name__ == "__main__":
    main()
