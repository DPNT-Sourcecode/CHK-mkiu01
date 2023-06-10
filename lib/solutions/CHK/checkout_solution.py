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
    'K': 80,
    'L': 90,
    'M': 15,
    'N': 40,
    'O': 10,
    'P': 50,
    'Q': 30,
    'R': 50,
    'S': 30,
    'T': 20,
    'U': 40,
    'V': 50,
    'W': 20,
    'X': 90,
    'Y': 10,
    'Z': 50,
}

# Special offers applying to individual SKUs
# List of tuples: number of items, item SKU, discounted price
special_offers_discount = [(5, 'A', 200), (3, 'A', 130), (2, 'B', 45)]

# Special offers giving a free item when other items are purchased
# List of tuples: number of items, item SKU, free SKU
special_offers_free_item = [(2, 'E', 'B'), (2, 'F', 'F')]

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

    return total


