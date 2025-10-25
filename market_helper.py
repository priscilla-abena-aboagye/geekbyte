print("Welcome to Kofi's Market Helper!")

shopkeeper = input("Your name: ")
item = input("Item bought: ")
price = float(input("What is the price of the item: "))
quantity = float(input("How many was bought?: "))
amount = float(input("Amount of money received: "))

total_cost = price * quantity
change = amount - total_cost

print("\n----- Receipt Summary -----")
print(f"Shopkeeper: {shopkeeper}")
print(f"Item bought: {item}")
print(f"Total cost: GHS {total_cost:.2f}")
print(f"Money received: GHS {amount:.2f}")
print(f"Change to give back: GHS {change:.2f}")

print("\nThank you for using Kofi's Market Helper!")
