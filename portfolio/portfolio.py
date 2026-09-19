class Holding:
    def __init__(self, ticker: str, quantity: int, avg_cost: float, current_price: float = 0.0):
        self.ticker = ticker
        self.quantity = quantity
        self.avg_cost = avg_cost
        self.current_price = current_price

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
        remainder = self.cash - total_cost
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

    def sell(self, date: str, ticker: str, quantity: int, price: float):
        if ticker not in self.holdings or self.holdings[ticker].quantity < quantity:
            raise ValueError(f"you dont have enough {ticker} to complete operation")

        proceeds = quantity * price
        self.cash += proceeds
        self.holdings[ticker].quantity -= quantity

        if self.holdings[ticker].quantity == 0:
            del self.holdings[ticker]

        self.transactions.append(Transaction(date, ticker, "SELL", quantity, price))

    def value(self):
        total = self.cash
        for ticker in self.holdings:
            total += (self.holdings[ticker].quantity * self.holdings[ticker].current_price)
        return total

    def profit_loss(self):
        total_value = 0
        total_cost = 0
        for ticker in self.holdings:
            total_value += (self.holdings[ticker].quantity * self.holdings[ticker].current_price)
        for ticker in self.holdings:
            total_cost += (self.holdings[ticker].avg_cost * self.holdings[ticker].quantity )
        return total_value - total_cost

    def allocation(self):
        total = self.cash
        for ticker in self.holdings:
            total += (self.holdings[ticker].quantity * self.holdings[ticker].current_price)
        cash = self.cash / total
        print(f"CASH {cash * 100}%")
        for ticker in self.holdings:
            percentage = (self.holdings[ticker].quantity * self.holdings[ticker].current_price) / total
            print(f"{ticker} {percentage * 100}%")
        return
