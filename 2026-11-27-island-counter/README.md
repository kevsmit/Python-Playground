# Island Counter

Reads a little text map and counts how many islands are in it.
`#` is land and `.` is water. Land touching up/down/left/right
counts as the same island, diagonals don't.

It uses a flood fill (BFS) from each unvisited land cell. Prints
the map with each island labeled by a letter, then the sizes
biggest first.

## Run

    python islands.py map.txt

Make your own map in any text file, just use `#` and `.`.
