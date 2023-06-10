sku_prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}

# Special offers dict mapping item to a tuple (count, price), for offers applying to individual SKUs
special_offers = [(5, 'A', 200), (3, 'A', 130), (2, 'B', 45)]

# Special offers giving a free item when other items are purchased
# dict mapping the purchased item to a tuple (count required, other item which is free)
special_offers_free_item = {'E': (2, 'B')}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # dict mapping item to its count in the basket
    basket = {}
    for item in skus:
        if item in basket:
            basket[item] += 1
        else:
            basket[item] = 1
    # sum up the total
    total = 0
    for item, count in basket.items():
        if item in sku_prices.keys():
            total += sku_prices[item] * count
        else:
            return -1

    # calculate discount for special offers
    for special_offer in special_offers:
        offer_count, item, offer_price = special_offer
        if item in basket:
            while basket[item] >= offer_count:
                # calculate the discount
                full_price = sku_prices[item] * offer_count
                discount = full_price - offer_price
                total -= discount
                # remove item from the basket after calculating the discount
                basket[item] -= offer_count

    #for item, count in basket.items():
    #    if item in special_offers:
    #        # how many times are we repeating the offer in the basket
    #        num_offers = count // special_offers[item][0]
    #        discount = num_offers * (sku_prices[item] * num_offers - special_offers[item][1])
    #        total -= discount

    # calculate discount for more offers
    for item, count in basket.items():
        if item in special_offers_free_item.keys():
            # how many times can we repeat the offer
            num_offers = basket[item] // special_offers_free_item[item][0]
            # calculate how many times we can actually do the discount (ensure that we have enough of the free items in the basket)
            free_item = special_offers_free_item[item][1]
            num_of_free_items = 0
            if free_item in basket:
                num_of_free_items = basket[free_item] 
            discounted_items = min(num_offers, num_of_free_items)
            # calculate the discount
            discount = sku_prices[free_item] * discounted_items
            total -= discount

    return total





