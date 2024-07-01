import art2

print(art2.logo)
print("Welcome to the secret auction!")

auction = {}

choice = True

while choice:
    name = input("What is your name? ")
    bid = int(input("How much would you like to bid? $"))
    auction[name] = bid
    choice = input("Are there any new bidders? ")

    if choice == "no":
        choice = False


highest_bidder = max(auction, key=auction.get)

bid_value = auction[highest_bidder]

print(f'\nThe winner is {highest_bidder} with a bid of ${bid_value}.')
