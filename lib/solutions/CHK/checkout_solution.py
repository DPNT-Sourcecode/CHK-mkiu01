sku_prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}

# Special offers dict mapping item to a tuple (count, price), for offers applying to individual SKUs
#special_offers = {'A': (3, 130), 'B': (2, 45)}
special_offers = [(5, 'A', 200), (3, 'A', 130), (2, 'B', 45)]

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
            #if item in special_offers:
            #    # how many times are we repeating the offer in the basket
            #    num_offers = count // special_offers[item][0]
            #    # any additional item that we can't group in the offer
            #    leftover_count = count % special_offers[item][0]
            #    total += num_offers * special_offers[item][1] + leftover_count * sku_prices[item]
            #else:
            total += sku_prices[item] * count
        else:
            return -1

    # calculate discount for special offers
    for special_offer in special_offers:
        count, item, price = special_offer
        if item in item_counts:
            pass

    for item, count in item_counts.items():
        if item in special_offers:
            # how many times are we repeating the offer in the basket
            num_offers = count // special_offers[item][0]
            discount = num_offers * (sku_prices[item] * num_offers - special_offers[item][1])
            total -= discount

    # calculate discount for more offers
    for item, count in item_counts.items():
        if item in special_offers_free_item.keys():
            # how many times can we repeat the offer
            num_offers = item_counts[item] // special_offers_free_item[item][0]
            # calculate how many times we can actually do the discount (ensure that we have enough of the free items in the basket)
            free_item = special_offers_free_item[item][1]
            num_of_free_items = 0
            if free_item in item_counts:
                num_of_free_items = item_counts[free_item] 
            discounted_items = min(num_offers, num_of_free_items)
            # calculate the discount
            discount = sku_prices[free_item] * discounted_items
            total -= discount

    return total



