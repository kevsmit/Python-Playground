# Morse Code

Turns text into Morse code and Morse code back into text.

It figures out which way to go on its own: if the input is only dots,
dashes, spaces and slashes it decodes, otherwise it encodes.

Letters are split by spaces and words are split by ` / `.

## Run

    python morse.py hello world
    python morse.py ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."

Run it with no arguments to see a few examples.
