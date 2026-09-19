from portfolio.portfolio import Holding, Transaction, Portfolio


# -------------------------
# Test 1: Initial portfolio
# -------------------------

portfolio = Portfolio(10_000)

assert portfolio.cash == 10_000
assert len(portfolio.holdings) == 0
assert portfolio.value() == 10_000

print("Test 1 passed")


# -------------------------
# Test 2: Buy one stock
# -------------------------

portfolio = Portfolio(10_000)

portfolio.buy("2026-09-19", "AAPL", 10, 100)
portfolio.holdings["AAPL"].current_price = 120

assert portfolio.cash == 9_000
assert portfolio.holdings["AAPL"].quantity == 10
assert portfolio.holdings["AAPL"].avg_cost == 100
assert portfolio.holdings["AAPL"].current_price == 120

assert portfolio.value() == 10_200
assert portfolio.profit_loss() == 200

print("Test 2 passed")


# -------------------------
# Test 3: Price decreases
# -------------------------

portfolio.holdings["AAPL"].current_price = 80

assert portfolio.value() == 9_800
assert portfolio.profit_loss() == -200

print("Test 3 passed")


# -------------------------
# Test 4: Multiple holdings
# -------------------------

portfolio = Portfolio(10_000)

portfolio.buy("2026-09-19", "AAPL", 10, 100)
portfolio.buy("2026-09-19", "MSFT", 10, 50)

portfolio.holdings["AAPL"].current_price = 120
portfolio.holdings["MSFT"].current_price = 60

assert portfolio.cash == 8_500

assert portfolio.holdings["AAPL"].quantity == 10
assert portfolio.holdings["MSFT"].quantity == 10

assert portfolio.value() == 10_300
assert portfolio.profit_loss() == 300

print("Test 4 passed")


# -------------------------
# Test 5: Buy more of AAPL
# -------------------------

portfolio = Portfolio(10_000)

portfolio.buy("2026-09-19", "AAPL", 10, 100)
portfolio.buy("2026-09-19", "AAPL", 10, 120)

assert portfolio.cash == 7_800
assert portfolio.holdings["AAPL"].quantity == 20
assert portfolio.holdings["AAPL"].avg_cost == 110

portfolio.holdings["AAPL"].current_price = 130

assert portfolio.value() == 10_400
assert portfolio.profit_loss() == 400

print("Test 5 passed")


# -------------------------
# Test 6: Partial sale
# -------------------------

portfolio.sell("2026-09-19", "AAPL", 5, 130)

assert portfolio.cash == 8_450
assert portfolio.holdings["AAPL"].quantity == 15
assert portfolio.holdings["AAPL"].avg_cost == 110

print("Test 6 passed")


# -------------------------
# Test 7: Sell entire position
# -------------------------

portfolio.sell("2026-09-19", "AAPL", 15, 130)

assert "AAPL" not in portfolio.holdings
assert portfolio.cash == 10_400
assert portfolio.value() == 10_400

print("Test 7 passed")


# -------------------------
# Test 8: Not enough cash
# -------------------------

portfolio = Portfolio(1_000)

try:
    portfolio.buy("2026-09-19", "AAPL", 10, 200)
    assert False, "Expected ValueError"
except ValueError:
    pass

assert portfolio.cash == 1_000
assert len(portfolio.holdings) == 0

print("Test 8 passed")


# -------------------------
# Test 9: Not enough shares
# -------------------------

portfolio = Portfolio(10_000)

portfolio.buy("2026-09-19", "AAPL", 5, 100)

try:
    portfolio.sell("2026-09-19", "AAPL", 10, 120)
    assert False, "Expected ValueError"
except ValueError:
    pass

assert portfolio.holdings["AAPL"].quantity == 5

print("Test 9 passed")


# -------------------------
# Test 10: Transaction history
# -------------------------

portfolio = Portfolio(10_000)

portfolio.buy("2026-09-19", "AAPL", 10, 100)
portfolio.buy("2026-09-19", "MSFT", 5, 200)
portfolio.sell("2026-09-19", "AAPL", 3, 120)

assert len(portfolio.transactions) == 3

assert portfolio.transactions[0].action == "BUY"
assert portfolio.transactions[0].ticker == "AAPL"
assert portfolio.transactions[0].quantity == 10
assert portfolio.transactions[0].price == 100

assert portfolio.transactions[1].action == "BUY"
assert portfolio.transactions[1].ticker == "MSFT"

assert portfolio.transactions[2].action == "SELL"
assert portfolio.transactions[2].ticker == "AAPL"
assert portfolio.transactions[2].quantity == 3
assert portfolio.transactions[2].price == 120

print("Test 10 passed")


print("\nAll tests passed!")
