from portfolio.portfolio import Holding, Transaction, Portfolio


# Create a holding
apple = Holding("AAPL", 10, 180)

print("Holding:")
print(apple.ticker)
print(apple.quantity)
print(apple.avg_cost)


# Create a transaction
transaction = Transaction(
    "2026-08-29",
    "AAPL",
    "BUY",
    10,
    180
)

print("\nTransaction:")
print(transaction.date)
print(transaction.ticker)
print(transaction.action)
print(transaction.quantity)
print(transaction.price)


# Create a portfolio
portfolio = Portfolio(10000)

print("\nPortfolio:")
print("Cash:", portfolio.cash)
print("Holdings:", portfolio.holdings)
print("Transactions:", portfolio.transactions)
