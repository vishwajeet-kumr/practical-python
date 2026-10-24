import csv
from pprint import pprint


def read_portfolio(filename):
    """It reads holding stocks in the list of dictionaries
    with the keys name, shares and price in the portfolio"""

    portfolio = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)

        for row in rows:
            records = dict(zip(headers, row))
            stocks = {
                "name": records["name"],
                "shares": int(records["shares"]),
                "price": float(records["price"]),
            }
            portfolio.append(stocks)
    return portfolio


def read_prices(filename):
    """Read a CSV file of price data into
    a dict mapping names to prices."""
    prices = {}
    with open(filename) as file:
        rows = csv.reader(file)

        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return prices


def make_report_data(portfolio, prices):
    """It makes a list (name, price, current_price change) from
    portfolio and current market prices"""
    report_list = []

    for stock in portfolio:
        current_price = prices[stock["name"]]
        price_change = current_price - stock["price"]

        summary = (stock["name"], stock["price"], current_price, price_change)
        report_list.append(summary)

    return report_list


def print_report(report_data):
    headers = ("Name", "Shares", "Price", "Change")
    print("%10s %10s %10s %10s" % headers)
    print(("-" * 10 + " ") * len(headers))

    for row in report_data:
        print("%10s %10d %10.2f %10.2f" % row)


def portfolio_report(portfolio_file, price_file):
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(price_file)

    report = make_report_data(portfolio, prices)

    print_report(report)


print(portfolio_report("Work/Data/portfolio.csv", "Work/Data/prices.csv"))
