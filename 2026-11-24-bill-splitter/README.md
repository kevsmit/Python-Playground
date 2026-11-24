# Bill Splitter

Splits shared costs evenly and tells you who needs to pay who.
Useful after a trip or a dinner where different people paid for
different stuff.

Put the expenses in a CSV file like this:

    name,amount,description
    Sam,120.00,cabin deposit
    Jess,45.50,groceries
    Ana,0,

Anyone who didn't pay anything still needs a row with 0 so they
get counted in the split.

## Run

    python bill_splitter.py sample.csv
