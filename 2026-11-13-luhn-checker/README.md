# Luhn Checker

Checks if a number passes the Luhn checksum, the simple math check
used on credit card numbers and some ID numbers to catch typos.

It doesn't mean a card is real, just that the digits add up right.

Spaces and dashes are ignored.

## Run

    python luhn.py 79927398713
    python luhn.py 4539-1488-0343-6467

Get the last digit that would make a number valid:

    python luhn.py --digit 7992739871

Run it with no arguments to see a few examples.
