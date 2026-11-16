# Game of Life

Conway's Game of Life in the terminal.

Starts with a random 20x40 grid and runs the usual rules:
a live cell with 2 or 3 neighbors stays alive, a dead cell with
exactly 3 neighbors comes alive, everything else dies. Edges wrap around.

## Run

    python life.py

Runs 50 generations by default. Pass a number to run more or less:

    python life.py 200
