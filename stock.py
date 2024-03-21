import requests
import json
import time

class Stock:
    def __init__(self, symbol, shares, purchase_price):
        self.symbol = symbol
        self.shares = shares
        self.purchase_price = purchase_price

    def __str__(self):
        return f"{self.symbol}: {self.shares} shares purchased at ${self.purchase_price:.2f} per share"

class PortfolioTracker:
    def __init__(self):
        self.portfolio = []

    def add_stock(self, stock):
        self.portfolio.append(stock)

    def remove_stock(self, symbol):
        for stock in self.portfolio:
            if stock.symbol == symbol:
                self.portfolio.remove(stock)
                print(f"{symbol} removed from the portfolio.")
                return
        print(f"{symbol} not found in the portfolio.")

    def track_performance(self, current_prices):
        total_investment = 0
        current_value = 0

        for stock in self.portfolio:
            if stock.symbol in current_prices:
                total_investment += stock.shares * stock.purchase_price
                current_value += stock.shares * current_prices[stock.symbol]
                print(f"{stock.symbol}: Purchased at ${stock.purchase_price:.2f}, Current price: ${current_prices[stock.symbol]:.2f}")

        if total_investment == 0:
            print("No stocks in the portfolio.")
        else:
            profit_loss = current_value - total_investment
            print(f"Total Investment: ${total_investment:.2f}")
            print(f"Current Value: ${current_value:.2f}")
            print(f"Profit/Loss: ${profit_loss:.2f}")

def fetch_stock_prices(symbols):
    API_KEY = "YOUR_API_KEY"
    prices = {}

    for symbol in symbols:
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}"
        response = requests.get(url)
        data = response.json()
        try:
            price = float(data["Global Quote"]["05. price"])
            prices[symbol] = price
        except KeyError:
            print(f"Failed to fetch data for {symbol}")

    return prices

def automate_portfolio_update():
    symbols = ["AAPL", "GOOG", "MSFT"]  # Example list of stock symbols in the portfolio

    portfolio_tracker = PortfolioTracker()

    # Assuming the initial purchase details are already known
    stock1 = Stock("AAPL", 10, 150.50)
    stock2 = Stock("GOOG", 5, 2000.00)
    portfolio_tracker.add_stock(stock1)
    portfolio_tracker.add_stock(stock2)

    while True:
        current_prices = fetch_stock_prices(symbols)
        portfolio_tracker.track_performance(current_prices)
        print("Updating prices in 60 seconds...")
        time.sleep(60)  # Update prices every 60 seconds

# Run the automation
automate_portfolio_update()
