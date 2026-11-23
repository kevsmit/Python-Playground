# Code Breaker

Little guessing game. The computer picks a 4 digit code using the
digits 1-6 and you try to figure it out in 10 guesses.

After each guess you get hints:

- `+` a digit is right and in the right spot
- `-` a digit is in the code but in the wrong spot

## Run

    python code_breaker.py

You can pass a number to get the same code every time (handy for testing):

    python code_breaker.py 42
