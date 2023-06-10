import re

items = []

with open("prices.txt") as file:
    while line := file.readline():
        items.append([x.strip() for x in line.rstrip().split("|") if x])

print("sku_prices = {")
for item in items:
    print(f"    '{item[0]}': {item[1]},")
print("}")

offer_discount_list = []
for item in items:
    special_offers = item[2]
    if len(special_offers)>0:
        for special_offer in special_offers.split(", "):
            print(special_offer)
            parse_offer = re.match("(\d+)([A-Z]) for (\d+)", special_offer)
            if parse_offer:
                offer_discount_list.append((int(parse_offer.group(1)), parse_offer.group(2), int(parse_offer.group(3))))

offer_discount_list.sort(key=lambda item: (item[1], -int(item[0])))
print(offer_discount_list)

print("special_offers_discount = {")
#    print(f"    '{item[0]}': {item[1]},")
#print("}")