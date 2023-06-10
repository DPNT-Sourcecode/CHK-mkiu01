import re

items = []

with open("prices2.txt") as file:
    while line := file.readline():
        items.append([x.strip() for x in line.rstrip().split("|") if x])

print("sku_prices = {")
for item in items:
    print(f"    '{item[0]}': {item[1]},")
print("}")

offer_discount_list = []
offer_free_list = []
for item in items:
    special_offers = item[2]
    if len(special_offers)>0:
        for special_offer in special_offers.split(", "):
            m = re.match("(\d+)([A-Z]) for (\d+)", special_offer)
            if m:
                offer_discount_list.append((int(m.group(1)), m.group(2), int(m.group(3))))
            m = re.match("(\d+)([A-Z]) get one ([A-Z]) free", special_offer)
            if m:
                offer_free_list.append((int(m.group(1)), m.group(2), m.group(3)))

offer_discount_list.sort(key=lambda item: (item[1], -int(item[0])))

print("special_offers_discount = [")
for o in offer_discount_list:
    print(f"    ({o[0]}, '{o[1]}', {o[2]}),")
print("]")

print("special_offers_free_item = [")
for o in offer_free_list:
    print(f"    ({o[0]}, '{o[1]}', '{o[2]}'),")
print("]")

