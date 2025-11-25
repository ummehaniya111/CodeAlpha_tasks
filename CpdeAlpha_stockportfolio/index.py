# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 320
}

# Empty values to be filled later
portfolio = {}
total_value = 0

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()

     # Check if user wants to stop
    if stock == "DONE":
        break

     # Check if stock is valid
    if stock not in stock_prices:
        print("Stock not found in price list. Try again.")
        continue

    quantity = int(input(f"Enter quantity for {stock}: "))

    # saving it in portfolio dictionary
    portfolio[stock] = quantity

    # calculate the total value of all stocks in portfolio
    total_value += stock_prices[stock] * quantity

print("\n----------------------------")
print("Your Portfolio Summary")
print("----------------------------")

# s is stock, q is quantity in portfolio
for s, q in portfolio.items():
    print(f"stock: {s}, Quantity: {q}, Total Value: ${stock_prices[s] * q}")

print("\nTotal Investment Value:", total_value)

# Saving result to a file
save = input("\nDo you want to save this to a file? (yes/no): ").lower()

if save == "yes":
    filename = input("Enter filename (example: portfolio.txt or portfolio.csv): ")
    with open(filename, "w") as file:
        file.write("Stock,Quantity,Unit Price,Total Value\n")
        for s, q in portfolio.items():
            file.write(f"{s},{q},{stock_prices[s]}: {stock_prices[s] * q}\n")
        file.write(f"\nTotal Investment,{total_value}")
    print("File saved successfully!")
