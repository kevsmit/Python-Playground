"""Build an n x n matrix filled in a spiral and print it neatly."""
import sys


def spiral_matrix(n):
    grid = [[0] * n for _ in range(n)]
    top, bottom, left, right = 0, n - 1, 0, n - 1
    num = 1
    while top <= bottom and left <= right:
        for c in range(left, right + 1):
            grid[top][c] = num
            num += 1
        top += 1
        for r in range(top, bottom + 1):
            grid[r][right] = num
            num += 1
        right -= 1
        if top <= bottom:
            for c in range(right, left - 1, -1):
                grid[bottom][c] = num
                num += 1
            bottom -= 1
        if left <= right:
            for r in range(bottom, top - 1, -1):
                grid[r][left] = num
                num += 1
            left += 1
    return grid


def main():
    if len(sys.argv) > 1:
        text = sys.argv[1]
    else:
        text = input("Size of the matrix: ")
    if not text.isdigit() or int(text) < 1:
        print("Please enter a whole number of 1 or more.")
        return
    n = int(text)
    grid = spiral_matrix(n)
    width = len(str(n * n))
    for row in grid:
        print(" ".join(str(v).rjust(width) for v in row))


if __name__ == "__main__":
    main()
