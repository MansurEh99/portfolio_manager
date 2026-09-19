import math

from portfolio.portfolio import Portfolio


def test_buy():
    portfolio = Portfolio(10_000)

    portfolio.buy("2026-01-01", "AAPL", 50, 100)

    assert portfolio.cash == 5_000
    assert "AAPL" in portfolio.holdings
    assert portfolio.holdings["AAPL"].quantity == 50
    assert portfolio.holdings["AAPL"].avg_cost == 100


def test_multiple_buys():
    portfolio = Portfolio(10_000)

    portfolio.buy("2026-01-01", "AAPL", 50, 100)
    portfolio.buy("2026-01-02", "AAPL", 50, 120)

    assert portfolio.holdings["AAPL"].quantity == 100
    assert math.isclose(
        portfolio.holdings["AAPL"].avg_cost,
        110
    )
    assert portfolio.cash == 4_000


def test_buy_different_stocks():
    portfolio = Portfolio(10_000)

    portfolio.buy("2026-01-01", "AAPL", 50, 100)
    portfolio.buy("2026-01-01", "MSFT", 30, 100)

    assert "AAPL" in portfolio.holdings
    assert "MSFT" in portfolio.holdings

    assert portfolio.holdings["AAPL"].quantity == 50
    assert portfolio.holdings["MSFT"].quantity == 30
    assert portfolio.cash == 2_000


def test_buy_not_enough_cash():
    portfolio = Portfolio(1_000)

    try:
        portfolio.buy("2026-01-01", "AAPL", 20, 100)
        assert False
    except ValueError:
        assert True


def test_sell():
    portfolio = Portfolio(10_000)

    portfolio.buy("2026-01-01", "AAPL", 50, 100)
    portfolio.sell("2026-01-02", "AAPL", 20, 120)

    assert portfolio.cash == 7_400
    assert portfolio.holdings["AAPL"].quantity == 30


def test_sell_entire_position():
    portfolio = Portfolio(10_000)

    portfolio.buy("2026-01-01", "AAPL", 50, 100)
    portfolio.sell("2026-01-02", "AAPL", 50, 120)

    assert "AAPL" not in portfolio.holdings
    assert portfolio.cash == 10_000


def test_sell_too_many_shares():
    portfolio = Portfolio(10_000)

    portfolio.buy("2026-01-01", "AAPL", 50, 100)

    try:
        portfolio.sell("2026-01-02", "AAPL", 60, 120)
        assert False
    except ValueError:
        assert True


def test_sell_stock_not_owned():
    portfolio = Portfolio(10_000)

    try:
        portfolio.sell("2026-01-02", "AAPL", 10, 120)
        assert False
    except ValueError:
        assert True


def test_value():
    portfolio = Portfolio(10_000)

    portfolio.buy("2026-01-01", "AAPL", 50, 100)
    portfolio.buy("2026-01-01", "MSFT", 30, 100)

    portfolio.holdings["AAPL"].current_price = 110
    portfolio.holdings["MSFT"].current_price = 90

    assert portfolio.value() == 10_100


def test_profit_loss():
    portfolio = Portfolio(10_000)

    portfolio.buy("2026-01-01", "AAPL", 50, 100)

    portfolio.holdings["AAPL"].current_price = 110

    assert portfolio.profit_loss() == 500


def test_allocation():
    portfolio = Portfolio(10_000)

    portfolio.buy("2026-01-01", "AAPL", 50, 100)
    portfolio.buy("2026-01-01", "MSFT", 30, 100)

    portfolio.holdings["AAPL"].current_price = 100
    portfolio.holdings["MSFT"].current_price = 100

    allocation = portfolio.allocation()

    assert math.isclose(allocation["CASH"], 0.20)
    assert math.isclose(allocation["AAPL"], 0.50)
    assert math.isclose(allocation["MSFT"], 0.30)

    assert math.isclose(sum(allocation.values()), 1.0)


def test_transactions():
    portfolio = Portfolio(10_000)

    portfolio.buy("2026-01-01", "AAPL", 50, 100)
    portfolio.sell("2026-01-02", "AAPL", 20, 120)

    assert len(portfolio.transactions) == 2

    assert portfolio.transactions[0].action == "BUY"
    assert portfolio.transactions[0].ticker == "AAPL"
    assert portfolio.transactions[0].quantity == 50
    assert portfolio.transactions[0].price == 100

    assert portfolio.transactions[1].action == "SELL"
    assert portfolio.transactions[1].quantity == 20
    assert portfolio.transactions[1].price == 120

def test_buy_zero_quantity():
    portfolio = Portfolio(10_000)

    try:
        portfolio.buy("2026-01-01", "AAPL", 0, 100)
        assert False
    except ValueError:
        assert True


def test_buy_negative_quantity():
    portfolio = Portfolio(10_000)

    try:
        portfolio.buy("2026-01-01", "AAPL", -10, 100)
        assert False
    except ValueError:
        assert True


def test_buy_negative_price():
    portfolio = Portfolio(10_000)

    try:
        portfolio.buy("2026-01-01", "AAPL", 10, -100)
        assert False
    except ValueError:
        assert True


def test_sell_zero_quantity():
    portfolio = Portfolio(10_000)

    portfolio.buy("2026-01-01", "AAPL", 50, 100)

    try:
        portfolio.sell("2026-01-02", "AAPL", 0, 100)
        assert False
    except ValueError:
        assert True


def test_sell_negative_quantity():
    portfolio = Portfolio(10_000)

    portfolio.buy("2026-01-01", "AAPL", 50, 100)

    try:
        portfolio.sell("2026-01-02", "AAPL", -10, 100)
        assert False
    except ValueError:
        assert True


def test_sell_negative_price():
    portfolio = Portfolio(10_000)

    portfolio.buy("2026-01-01", "AAPL", 50, 100)

    try:
        portfolio.sell("2026-01-02", "AAPL", 10, -100)
        assert False
    except ValueError:
        assert True

print("All portfolio tests passed!")
