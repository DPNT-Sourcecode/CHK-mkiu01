
items = []

with open("prices.txt") as file:
    while line := file.readline():
        items.append([x.strip() for x in line.rstrip().split("|") if x])

print(items)
print("sku_prices = {")
for item in items:
    print(f"    '{item[0]}': {item[1]},")
print("}")



