# # # report.py
# # #
# # # Exercise 2.4
import csv
from pprint import pprint


def read_portfolio(filename):
    portfolio = []
    # total = 0.0
    with open("Data/portfolio.csv", "rt") as file:
        rows = csv.reader(file)
        header = next(file)
        for row in rows:
            # record = dict(zip(header, row))
            # print (record)
            name = str(row[0])
            shares = int(row[1])
            price = float(row[2])
            dist_port = {"name": name, "shares": shares, "price": price}
            # total += shares*price
            # holdings = [name, shares, price]
            portfolio.append(dist_port)

    # print(total)
    return portfolio


my_portfolio = read_portfolio("Data/portfolio.csv")
# pprint(my_portfolio)


def read_prices(filename):
    stock_names = {}
    with open("Data/prices.csv", "r") as f:
        rows = csv.reader(f)

        for row in rows:
            if not row:
                continue
            stocks = str(row[0])
            prices = float(row[1])

            # dict_format = {'stocks':stocks, 'prices':prices}
            # stock_names.append(dict_format)
            stock_names[stocks] = prices
            # print (row)

    return stock_names


market_data = read_prices("Data/prices.csv")


def make_report(my_portfolio, market_data):
    report_list = []

    for holdings in my_portfolio:
        Name = holdings["name"]
        Shares = holdings["shares"]
        original_price = holdings["price"]
        current_price = market_data[Name]
        price_change = current_price - original_price
        tuple_rows = (Name, Shares, current_price, price_change)
        report_list.append(tuple_rows)
    return report_list


report = make_report(my_portfolio, market_data)

headers = ("Name", "Shares", "Price", "Change")
header_string = " ".join([f"{h:>10}" for h in headers])
print(header_string)

separator_string = " ".join(["-" * 10 for _ in headers])
print(separator_string)

for row in report:
    formatted_data = (
        f"{row[0]:>10} {row[1]:>10} {f'${row[2]:.2f}':>10} {f'${row[3]:.2f}':>10}"
    )
    print(formatted_data)


# now calculating the Gain and Loss from the above data of the stocks:

# total_cost = 0.0
# current_value = 0.0

# for holdings in my_portfolio:
#     total_cost += holdings['shares']*holdings['price']

#     current_price = market_data[holdings['name']]
#     current_value += holdings['shares'] * current_price

# print(f"Total Invested: ${total_cost:0.2f}")
# print(f"Current Value: ${current_value:0.2f}")
# print(f"Total Gain/Loss: ${(current_value - total_cost):0.2f}")


# print("------------- Individual Share Price Changes -------------")

# for holdings in my_portfolio:
#     name = holdings['name']
#     bought_price = holdings['price']

#     current_price = market_data[name]

#     price_change = current_price - bought_price

#     print(f"{name:>4} | Bought: ${bought_price:>6.2f} | Current: ${current_price:>6.2f} | Change: ${price_change:>7.2f}")
