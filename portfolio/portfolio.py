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

    def buy(self, date: str, ticker: str, quantity: int, cost: float):
        total_cost = cost * quantity
        remainder = self.cash - cost
        if remainder < 0:
            raise ValueError("Not enough cash")

        self.cash -= total_cost

        if ticker in self.holdings:
            old_cost = self.holdings[ticker].avg_cost
            old_quantity = self.holdings[ticker].quantity
            self.holdings[ticker].quantity += quantity
            self.holdings[ticker].avg_cost = ((old_quantity * old_cost) + (quantity * cost)) / self.holdings[ticker].quantity
        else:
            self.holdings[ticker] = Holding(ticker, quantity, cost)

        self.transactions.append(Transaction(date, ticker, "BUY", quantity, cost))

    def sell(self, date: str, ticker: str, quantity: float, price: int):
        if ticker not in self.holdings or self.holdings[ticker].quantity >= quantity:
            raise ValueError(f"you dont have enough {ticker} to complete operation")

        proceeds = quantity * price
        self.cash += proceeds
        self.holdings[ticker].quantity -= quantity

        if self.holdings[ticker].quantity == 0:
            del self.holdings[ticker]

        self.transactions.append(Transaction(date, ticker, "SELL", quantity, price))
