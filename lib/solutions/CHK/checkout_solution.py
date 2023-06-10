sku_prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}

# Special offers dict mapping item to a tuple (count, price)
special_offers = {'A': (3, 130), 'B': (2, 45)}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # dict mapping item to count in the basket
    item_counts = {}
    for item in skus:
        if item in item_counts:
            item_counts[item] += 1
        else:
            item_counts[item] = 1
    # sum up the total
    total = 0
    for item, count in item_counts.items():
        if item in sku_prices.keys():
            if item in special_offers:
                # how many times are we repeating the offer in the basket
                num_offers = count // special_offers[item][0]
                # any additional item that we can't group in the offer
                leftover_count = count % special_offers[item][0]
                total += num_offers * special_offers[item][1] + leftover_count * sku_prices[item]
            else:
                total += sku_prices[item] * count
        else:
            return -1
    return total
