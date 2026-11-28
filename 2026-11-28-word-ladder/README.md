# Word Ladder

Finds the shortest way to turn one word into another by changing
one letter at a time, where every step has to be a real word.
Like cold -> cord -> word -> ward -> warm.

It does a breadth first search so the first path it finds is
the shortest one. There's a small word list built in, or you
can pass your own file with one word per line.

## Run

    python ladder.py cold warm
    python ladder.py head beat
    python ladder.py cat dog mywords.txt
