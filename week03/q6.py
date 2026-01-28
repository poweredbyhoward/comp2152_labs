inventory = {
  # product : (price, quantity)
    "Laptop" : (999.99, 5),
    "Mouse" : (29.99, 15),
    "Keyboard" : (79.99, 10),
    "Monitor" : (299.99, 8)
}

prices = []
print("\t=== Current Inventory ===")
for item in inventory.items():
    (product, (price, quantity)) = item
    print(f"{product} - Price: ${price}, Quantity: {quantity}")
    prices.append(price)
print()

electronics = {"Laptop", "Monitor"}
accessories = {"Mouse", "Keyboard"}
all_categories = electronics | accessories

print(f"All product categories: {all_categories}")
print()

print(f"Price list: {prices}")
prices.sort()
print(f"Sorted prices: {prices}")
print(f"Lowest price: ${prices[0]}")
print(f"Highest price: ${prices[-1]}")
print()

inventory["Headphones"] = (49.99, 20)
inventory["Mouse"] = (29.99, 12)
del inventory["Monitor"]

print("\t=== Final Inventory ===")
for item in inventory.items():
    (product, (price, quantity)) = item
    print(f"{product} - Price: ${price}, Quantity: {quantity}")
    prices.append(price)


