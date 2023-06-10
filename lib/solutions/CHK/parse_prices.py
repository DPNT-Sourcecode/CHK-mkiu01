with open("prices.txt") as file:
    while line := file.readline():
        print(line.rsplit().split("|"))
