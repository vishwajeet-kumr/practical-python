# stock.py
class Stock:
    # __slots__ = ("name", "_shares", "_price")

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def shares(self):
        return self._shares

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Expected Integer")
        self._price = value
        if value < 0:
            raise ValueError("Price can't be negative.")

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError("Expected Integer")
        self._shares = value
        if value < 0:
            raise ValueError("Shares can't be negative.")

    @property
    def total_cost(self):
        """Total cost of the holdings: shares * price"""
        return self.shares * self.price

    def sell_share(self, num_shares):
        """Number of shares to sell"""
        self.shares -= num_shares

    def __repr__(self):
        return f"Stock({self.name!r}, {self.shares}, {self.price})"


if __name__ == "__main__":

    a = Stock("GOOG", 100, 95.50)
    b = Stock("AAPL", 50, 122.34)
    c = Stock("IBM", 75, 91.75)
    stocks = [a, b, c]

    for s in stocks:
        print(f"{s.name:>10s} {s.shares:>10d} {s.price:>10.2f}")
