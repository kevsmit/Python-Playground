# Markdown Table Maker

Takes a CSV file and prints it out as a markdown table so you can
paste it into a README or a GitHub comment without lining up all
the pipes by hand.

Columns that are all numbers get right aligned, the rest are left
aligned.

## Run

    python table_maker.py sample.csv

Output:

    | item         | store          | price | qty |
    | ------------ | -------------- | ----: | --: |
    | coffee beans | Corner Market  | 12.99 |   2 |
    | oat milk     | Grocery Outlet |  3.49 |   4 |
    | bagels       | Corner Market  |  6.00 |   1 |
