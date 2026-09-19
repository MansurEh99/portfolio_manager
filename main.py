from portfolio.portfolio import Portfolio
from performance.performance import Performance
from performance.risk import Risk
from report import Report

def main():
    # Create portfolio
    portfolio = Portfolio(10_000)

    # Buy holdings
    portfolio.buy("2026-01-01", "AAPL", 50, 100)
    portfolio.buy("2026-01-01", "MSFT", 30, 100)

    # Update current market prices
    portfolio.holdings["AAPL"].current_price = 110
    portfolio.holdings["MSFT"].current_price = 95

    # Create performance tracker
    performance = Performance(portfolio)

    # Record portfolio history
    performance.history["2026-01-01"] = 10_000
    performance.history["2026-01-02"] = 10_500
    performance.history["2026-01-03"] = 9_800
    performance.history["2026-01-04"] = 10_300
    performance.history["2026-01-05"] = 10_400
    performance.history["2026-01-06"] = 11_000

    # Create risk tracker
    risk = Risk(portfolio, performance)

    # Create report
    report = Report(
        portfolio,
        performance,
        risk
    )

    # Generate and display report
    output = report.full_report(
        risk_free=0.01,
        start_date="2026-01-01",
        end_date="2026-01-06"
    )

    print(output)

if __name__ == "__main__":
    main()
