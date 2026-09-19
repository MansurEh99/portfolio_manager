from portfolio.portfolio import Portfolio
from performance.performance import Performance
from performance.risk import Risk

class Report:
    def __init__(self, portfolio: Portfolio, performance: Performance, risk: Risk):
        self.portfolio = portfolio
        self.performance = performance
        self.risk = risk

    def full_report(self, risk_free, start_date, end_date):
        portfolio_value = self.portfolio.value()
        cash = self.portfolio.cash
        report = """========================================
                PORTFOLIO REPORT
        ========================================"""
        report += f"\n\nPortfolio Value:       ${portfolio_value:,.2f}"
        report += f"\nCash:                  ${cash:,.2f}"
        report += """\n\nHOLDINGS
        ----------------------------------------"""
        report += "\nTicker    Quantity    Price      Value"
        for ticker in self.portfolio.holdings:
            quantity = self.portfolio.holdings[ticker].quantity
            price = self.portfolio.holdings[ticker].current_price
            report += f"\n{ticker}         {quantity}       ${price:,.2f}      ${quantity * price:,.2f}"
        report += """\n\nPERFORMANCE
        ----------------------------------------"""
        total_return = self.performance.total_return(start_date, end_date)
        volatility = self.performance.volatility()
        max_drawdown = self.performance.maximum_drawdown()
        ratio = self.performance.sharpe_ratio(risk_free)
        report += f"\nTotal Return:          {round(total_return * 100, 2)}%"
        report += f"\nVolatility:            {round(volatility * 100, 2)}%"
        report += f"\nMaximum Drawdown:     {round(max_drawdown * 100, 2)}%"
        report += f"\nSharpe Ratio:           {round(ratio, 2)}"
        report += """\n\nRISK
        ----------------------------------------"""
        largest = self.risk.largest_position()
        largest_position = largest[0]
        largest_weight = largest[1]
        report += f"\nLargest Position:      {largest_position}"
        report += f"\nLargest Weight:       {largest_weight * 100}%"
        return report
