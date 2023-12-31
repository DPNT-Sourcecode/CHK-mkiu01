sku_prices = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
    'F': 10,
    'G': 20,
    'H': 10,
    'I': 35,
    'J': 60,
    'K': 70,
    'L': 90,
    'M': 15,
    'N': 40,
    'O': 10,
    'P': 50,
    'Q': 30,
    'R': 50,
    'S': 20,
    'T': 20,
    'U': 40,
    'V': 50,
    'W': 20,
    'X': 17,
    'Y': 20,
    'Z': 21,
}

# Special offers applying to individual SKUs
# List of tuples: number of items, item SKU, discounted price
special_offers_discount = [
    (5, 'A', 200),
    (3, 'A', 130),
    (2, 'B', 45),
    (10, 'H', 80),
    (5, 'H', 45),
    (2, 'K', 120),
    (5, 'P', 200),
    (3, 'Q', 80),
    (3, 'V', 130),
    (2, 'V', 90),
]

# Special offers giving a free item when other items are purchased
# List of tuples: number of items, item SKU, free SKU
special_offers_free_item = [
    (2, 'E', 'B'),
    (2, 'F', 'F'),
    (3, 'N', 'M'),
    (3, 'R', 'Q'),
    (3, 'U', 'U'),
]

group_discounts = [
    (3, ('S', 'T', 'X', 'Y', 'Z'), 45),
]

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
    # sum up the total, without discounts
    total = 0
    for item, count in basket.items():
        if item in sku_prices.keys():
            total += sku_prices[item] * count
        else:
            return -1

    # calculate discount for more offers (special offers with free items)
    for offer in special_offers_free_item:
        offer_count, item, free_item = offer
        if item in basket:
            while basket[item] >= (offer_count + 1 if item == free_item else offer_count):
                # check that we have the free item in the basket
                if free_item in basket and basket[free_item]>0:
                    discount = sku_prices[free_item]
                    total -= discount
                    basket[free_item] -= 1
                # remove items from the basket after calculating the discount
                basket[item] -= offer_count
                    
    # calculate discount for special offers
    for offer in special_offers_discount:
        offer_count, item, offer_price = offer
        if item in basket:
            while basket[item] >= offer_count:
                # calculate the discount
                full_price = sku_prices[item] * offer_count
                discount = full_price - offer_price
                total -= discount
                # remove item from the basket after calculating the discount
                basket[item] -= offer_count

    # calculate group discounts
    for offer in group_discounts:
        offer_count, any_item, offer_price = offer
        # count the items to discount in desc price order,
        # to ensure that we always favour the customer by giving the max discount
        sorted_any_item = list(any_item)
        sorted_any_item.sort(key=lambda item: sku_prices[item], reverse=True)
        # get all the potentially discounted items (ordered by price desc)
        discounted_items = []
        for item in sorted_any_item:
            if item in basket:
                discounted_items.extend([item] * basket[item])
        while len(discounted_items)>=offer_count:
            # get the current group
            current_group = discounted_items[:offer_count]
            # calculate the discount
            discount = sum([sku_prices[i] for i in current_group]) - offer_price
            total -= discount
            # remove the group from the list
            discounted_items = discounted_items[offer_count:]
        
    return total
