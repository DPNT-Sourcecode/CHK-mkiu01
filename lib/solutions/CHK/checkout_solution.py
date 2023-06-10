sku_prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}

# Special offers dict mapping item to a tuple (count, price)
special_offers = {'A': (3, 130), 'B': (2, 45)}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total = 0
    item_counts = {}
    for item in skus:
        if item in sku_prices.keys():
            total += sku_prices[item]
        else:
            return -1
    return total



