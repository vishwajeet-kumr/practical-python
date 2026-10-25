#stock.py
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def total_cost(self):
        """Total cost of the holdings: shares * price"""
        return self.shares * self.price

    def sell_share(self, num_shares):
        """Number of shares to sell"""
        self.shares -= num_shares


if __name__ == "__main__":

    a = Stock("GOOG", 100, 95.50)
    b = Stock("AAPL", 50, 122.34)
    c = Stock("IBM", 75, 91.75)
    stocks = [a, b, c]

    for s in stocks:
        print(f"{s.name:>10s} {s.shares:>10d} {s.price:>10.2f}")
