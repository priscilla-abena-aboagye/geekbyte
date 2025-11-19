supplier_A = {"tomato", "onion", "pepper", "yam", "plantain"} 
supplier_B = {"onion", "pepper", "cassava", "carrot", "tomato"} 

print("--------------------------------------")
# set operations 
print(supplier_A.intersection(supplier_B))
print(supplier_A.difference(supplier_B))
print(supplier_B.difference(supplier_A))
print(supplier_A.union(supplier_B))
print("--------------------------------------")
item_prices = {
    "onion": 10,
    "pepper": 12,
    "sugar": 5,
    "cabbage": 25,
    "oil": 36,
    "cup": 71
}
item = input("What would you like to buy?: ")
if item in item_prices: # checks for the presence of the item
    print(f"The price of {item} is {item_prices[item]}")
else: 
    print("Item not sold here")