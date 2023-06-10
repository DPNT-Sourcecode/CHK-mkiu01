sku_prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}

# Special offers dict mapping item to a tuple (count, price), for offers applying to individual SKUs
special_offers = {'A': (3, 130), 'B': (2, 45)}

# Special offers giving a free item when other items are purchased
# dict mapping the purchased item to a tuple (count required, other item which is free)
special_offers_free_item = {'E': (2, 'B')}


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


