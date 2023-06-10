with open("prices.txt") as file:
    while line := file.readline():
        item, price, offers = list(filter(None, line.rstrip().split("|")))
        print(f"{item}, {price}, {offers}")

