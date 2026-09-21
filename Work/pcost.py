# pcost.py
#
# Exercise 1.27
import csv

def portfolio_cost(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    total_cost = 0.0

    with open("/home/vishwajeet-kumar/Projects/BuildingMySelf/Python/practical-python/Work/Data/portfolio.csv", 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            nshares = int(row[1])
            price = float(row[2])
            total_cost += nshares * price
    print("total cost = ", total_cost)
portfolio_cost("/home/vishwajeet-kumar/Projects/BuildingMySelf/Python/practical-python/Work/Data/portfolio.csv")



































