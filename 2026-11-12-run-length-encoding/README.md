# Run-Length Encoding

Small script that squashes repeated letters into a count + letter,
and can turn it back again.

`AAABBBCCCCD` becomes `3A3B4C1D`.

Note: digits in the original text won't decode correctly since numbers
are used for the counts. Fine for letters and symbols.

## Run

    python rle.py encode AAABBBCCCCD
    python rle.py decode 3A3B4C1D

Run it with no arguments to see an example.
