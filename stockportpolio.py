import csv

def stock_portfolio_tracker():
    # Hardcoded stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOG": 135,
        "MSFT": 310,
        "AMZN": 140
    }

    portfolio = {}
    total_value = 0

    print("📊 Stock Portfolio Tracker")
    print("Available stocks:", ", ".join(stock_prices.keys()))

    while True:
        stock = input("Enter stock symbol (or 'done' to finish): ").upper()
        if stock == "DONE":
            break
        if stock not in stock_prices:
            print("⚠️ Stock not available. Try again.")
            continue

        try:
            qty = int(input(f"Enter quantity of {stock}: "))
        except ValueError:
            print("⚠️ Please enter a valid number.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + qty
        print(f"✅ Added {qty} shares of {stock}.")

    print("\n📌 Your Portfolio:")
    for stock, qty in portfolio.items():
        value = qty * stock_prices[stock]
        total_value += value
        print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}")

    print(f"\n💰 Total Investment Value: ${total_value}")

    # Save to CSV file
    save = input("\nDo you want to save portfolio to a CSV file? (y/n): ").lower()
    if save == "y":
        with open("portfolio.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Quantity", "Price", "Total Value"])
            for stock, qty in portfolio.items():
                writer.writerow([stock, qty, stock_prices[stock], qty * stock_prices[stock]])
            writer.writerow(["TOTAL", "", "", total_value])
        print("📁 Portfolio saved to portfolio.csv")


# Run the tracker
if __name__ == "__main__":
    stock_portfolio_tracker()
