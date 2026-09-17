# pcost.py
#
# Exercise 1.27

total_cost = 0.0
with open ('/home/vishwajeet-kumar/Projects/BuildingMySelf/Python/practical-python/Work/Data/portfolio.csv', 'rt') as f:
    headers = next(f)
    for line in f:
        row = line.split(',')
        print(row)
        share_name = row[0]
        units = int(row[1])
        price = float(row[2])
        total_cost = total_cost + (units*price)

print('Total Cost', total_cost)


