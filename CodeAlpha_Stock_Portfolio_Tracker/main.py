stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

total = 0

while True:
    stock = input("Enter Stock Name (or done): ").upper()

    if stock == "DONE":
        break

    if stock not in stocks:
        print("Stock not available")
        continue

    quantity = int(input("Quantity: "))

    value = stocks[stock] * quantity
    total += value

print("\nTotal Investment Value: $", total)

with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value: ${total}")

print("Saved to portfolio.txt")