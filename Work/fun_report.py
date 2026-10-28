#!/usr/bin/env python3
# fun_report.py
import sys
import stock
import fileparse
import tableformat


def read_portfolio(filename):
    """It reads holding stocks in the list of dictionaries
    with the keys name, shares and price in the portfolio"""

    # portfolio = []
    with open(filename) as file:
        #     rows = csv.reader(file)
        #     headers = next(rows)

        #     for row in rows:
        #         records = dict(zip(headers, row))
        #         stocks = {
        #             "name": records["name"],
        #             "shares": int(records["shares"]),
        #             "price": float(records["price"]),
        #         }
        #         portfolio.append(stocks)
        # return portfolio
        # #
        portdicts = fileparse.parse_csv(
            file,
            select=["name", "shares", "price"],
            types=[str, int, float],
            has_headers=True,
        )
    return [stock.Stock(d["name"], d["shares"], d["price"]) for d in portdicts]


def read_prices(filename):
    """Read a CSV file of price data into
    a dict mapping names to prices."""
    # prices = {}
    with open(filename) as file:
        #     rows = csv.reader(file)

        #     for row in rows:
        #         try:
        #             prices[row[0]] = float(row[1])
        #         except IndexError:
        #             pass
        # return prices
        #
        return dict(fileparse.parse_csv(file, types=[str, float], has_headers=False))


def make_report_data(portfolio, prices):
    """It makes a list (name, price, current_price change) from
    portfolio and current market prices"""
    report_list = []

    for s in portfolio:
        current_price = prices.get(s.name, 0.0)
        price_change = current_price - s.price

        summary = (s.name, s.shares, current_price, price_change)
        report_list.append(summary)

    return report_list


def print_report(report_data, formatter):

    formatter.headings(["name", "shares", "price", "change"])
    for name, shares, price, change in report_data:
        rowdata = [name, str(shares), f"{price:.2f}", f"{change:.2f}"]
        formatter.row(rowdata)

    # headers = ("Name", "Shares", "Price", "Change")
    # print("%10s %10s %10s %10s" % headers)
    # print(("-" * 10 + " ") * len(headers))

    # for row in report_data:
    #     print("%10s %10d %10.2f %10.2f" % row)


def portfolio_report(portfolio_file, price_file, fmt):
    # def main(argv):
    #     if len(argv) != 4:
    #         raise SystemExit("Must be 4 elements in the argv")
    portfolio = read_portfolio(portfolio_file)
    # portfolio = read_portfolio(argv[1])
    # prices = read_prices(argv[2])
    prices = read_prices(price_file)

    report = make_report_data(portfolio, prices)
    formatter = tableformat.create_formatter(fmt)

    print_report(report, formatter)


def main(argv):
    if len(argv) < 3:
        raise SystemExit(f"Usage: {argv[0]} portfile pricefile [fmt]")
    fmt = argv[3] if len(argv) == 4 else "txt"
    portfolio_report(argv[1], argv[2], fmt)


if __name__ == "__main__":
    main(sys.argv)
    # print(portfolio_report("Data/portfolio.csv", "Data/prices.csv"))
