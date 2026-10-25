#!/usr/bin/env python3
# pcost.py
#
# Exercise 1.27
import csv
import fun_report
import sys



# from pprint import pprint
def portfolio_cost(argv):
    # def main(argv):
    """Computes the total cost (shares*price) of a portfolio file"""

    portfolio = fun_report.read_portfolio(argv)
    return sum((s.shares * s.price for s in portfolio))

def main(argv):
    if len(argv) != 2:
        raise SystemExit(f'Usage: {argv[0]} portfile')
    cost = portfolio_cost(argv[1])
    print(f'Total cost: {cost:.2f}')


if __name__ == "__main__":
    main(sys.argv)
    # total_cost = 0.0

    # with open(filename, "rt") as f:
    #     rows = csv.reader(f)
    #     headers = next(rows)
    #     for rowno, row in enumerate(rows, start=1):
    #         record = dict(zip(headers, row))
    #         print(record)
    #         try:
    #             nshares = int(record["shares"])
    #             price = float(record["price"])
    #             total_cost += nshares * price
    #         except ValueError:
    #             print(f"Row {rowno}: Bad Row: {row}")

    # print("total cost = ", total_cost)
