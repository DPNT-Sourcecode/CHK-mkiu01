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
            total += sku_prices[item] * count
        else:
            return -1
    return total




