from portfolio.portfolio import Portfolio
from performance.performance import Performance
from performance.risk import Risk
from report import Report


def create_report():
    portfolio = Portfolio(10_000)

    portfolio.buy("2026-01-01", "AAPL", 50, 100)
    portfolio.buy("2026-01-01", "MSFT", 30, 100)

    portfolio.holdings["AAPL"].current_price = 100
    portfolio.holdings["MSFT"].current_price = 100

    performance = Performance(portfolio)

    performance.history["2026-01-01"] = 10_000
    performance.history["2026-01-02"] = 10_500
    performance.history["2026-01-03"] = 9_800
    performance.history["2026-01-04"] = 10_300
    performance.history["2026-01-05"] = 10_400
    performance.history["2026-01-06"] = 11_000

    risk = Risk(portfolio, performance)

    report = Report(
        portfolio,
        performance,
        risk
    )

    return report


def test_report_contains_title():
    report = create_report()

    output = report.portfolio_report(
        risk_free=0.01,
        start_date="2026-01-01",
        end_date="2026-01-06"
    )

    assert "PORTFOLIO REPORT" in output


def test_report_contains_portfolio_data():
    report = create_report()

    output = report.portfolio_report(
        risk_free=0.01,
        start_date="2026-01-01",
        end_date="2026-01-06"
    )

    assert "Portfolio Value" in output
    assert "Cash" in output

    assert "AAPL" in output
    assert "MSFT" in output

    assert "50" in output
    assert "30" in output


def test_report_contains_performance_data():
    report = create_report()

    output = report.portfolio_report(
        risk_free=0.01,
        start_date="2026-01-01",
        end_date="2026-01-06"
    )

    assert "PERFORMANCE" in output

    assert "Total Return" in output
    assert "Volatility" in output
    assert "Maximum Drawdown" in output
    assert "Sharpe Ratio" in output


def test_report_contains_risk_data():
    report = create_report()

    output = report.portfolio_report(
        risk_free=0.01,
        start_date="2026-01-01",
        end_date="2026-01-06"
    )

    assert "RISK" in output

    assert "Largest Position" in output
    assert "Largest Weight" in output

    assert "AAPL" in output


def test_report_contains_expected_values():
    report = create_report()

    output = report.portfolio_report(
        risk_free=0.01,
        start_date="2026-01-01",
        end_date="2026-01-06"
    )

    # Portfolio
    assert "$10,000.00" in output
    assert "$2,000.00" in output

    # Holdings
    assert "$5,000.00" in output
    assert "$3,000.00" in output

    # Risk
    assert "50.00%" in output


def test_report_is_string():
    report = create_report()

    output = report.portfolio_report(
        risk_free=0.01,
        start_date="2026-01-01",
        end_date="2026-01-06"
    )

    assert isinstance(output, str)


print("All report tests passed!")
