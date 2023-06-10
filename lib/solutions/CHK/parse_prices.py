
items = []

with open("prices.txt") as file:
    while line := file.readline():
        items.append([x.strip() for x in line.rstrip().split("|") if x])

print("sku_prices = {")
for item in items:
    print(f"    '{item[0]}': {item[1]},")
print("}")

print("special_offers_discount = {")
for item in items:
    special_offers = item[2]
    if len(special_offers)>0:
        for special_offer in special_offers.split(", "):
            print(special_offer)
#    print(f"    '{item[0]}': {item[1]},")
#print("}")



