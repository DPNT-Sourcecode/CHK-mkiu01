

sku_prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total = 0
    for item in skus:
        if item in sku_prices.keys():
            total += sku_prices[item]
        else:
            return -1
    return total


