# Sudoku Solver

Solves a sudoku using plain backtracking. It fills the first empty cell
with the first number that fits, moves on, and backs up when it gets stuck.

Runs a built-in puzzle if you don't give it a file.

## Run

    python sudoku.py
    python sudoku.py my_puzzle.txt

Puzzle file is 9 lines of 9 digits. Use 0 or . for blanks:

    53..7....
    6..195...
    .98....6.
    ...
