STOCK_PRICES = {"AAPL": 180, "TSLA": 250, "GOOGL": 140, "MSFT": 330}


def main():
    print("Available stocks:", ", ".join(STOCK_PRICES))
    portfolio = {}

    while True:
        name = input("Stock name (or 'done'): ").upper().strip()
        if name == "done".upper():
            break
        if name not in STOCK_PRICES:
            print("That stock isn't in the price list.")
            continue
        try:
            qty = int(input("Quantity: "))
        except ValueError:
            print("Enter a whole number.")
            continue
        portfolio[name] = portfolio.get(name, 0) + qty

    total = 0
    lines = []
    for name, qty in portfolio.items():
        value = STOCK_PRICES[name] * qty
        total += value
        lines.append(f"{name}: {qty} x {STOCK_PRICES[name]} = {value}")

    lines.append(f"Total investment: {total}")
    print("\n" + "\n".join(lines))

    if input("\nSave to file? (y/n): ").lower().strip() == "y":
        with open("portfolio.txt", "w") as f:
            f.write("\n".join(lines))
        print("Saved to portfolio.txt")


if __name__ == "__main__":
    main()