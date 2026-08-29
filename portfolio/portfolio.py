class Holding:
    def __init__(self, ticker: str, quantity: int, avg_cost: float):
        self.ticker = ticker
        self.quantity = quantity
        self.avg_cost = avg_cost

class Transaction:
    def __init__(self, date: str, ticker: str, action: str, quantity: int, price: float):
        self.date = date
        self.ticker = ticker
        self.action = action
        self.quantity = quantity
        self.price = price

class Portfolio:
    def __init__(self, cash: float):
        self.cash = cash
        self.holdings = {}
        self.transactions = []
