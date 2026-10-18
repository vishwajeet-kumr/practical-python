# pcost.py
#
# Exercise 1.27
import csv
# from pprint import pprint
def portfolio_cost(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            print(record)
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            except ValueError:
                print(f'Row {rowno}: Bad Row: {row}')
                
    print("total cost = ", total_cost)
    
portfolio_cost("Work/Data/portfoliodate.csv")
