# name = 'IBM'
# shares = 100
# price = 91.5

# print(f'{name:>10s} {shares:>10d} {price:>10.2f}')

# s = {
#     'name': 'IBM', 
#     'shares': 200,
#     'price': 91.1
# }

# print ('{name:>10s} {shares:>10d} {price:>10.2f}'.format_map(s))

# value = 234324.2343
# print ( f'{value:*>20,.2f}')
# frmt = '%20.2f' % value
# print ( frmt)

import csv
def read_prices(filename):
    prices = {}
    with open(filename) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            prices[row[0]] = float[row[1]]
    return prices
oldprices = read_prices('oldprices.csv')
newprices = read_prices('newprices.csv')