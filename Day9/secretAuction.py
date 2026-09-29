# First-pricesealed-bid auction
# Blind Auction

# one person enters their name and bid
# clear the screen for the next person

from auction_art import logo, win
print(logo)

def highest_bid(bidding_record):
    max_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > max_bid:
            max_bid = bid_amount
            winner = bidder
    print(win)
    print(f"The winner is {winner} with a bid of {max_bid}. Congratulations!!!")

bid = {}
choice = "yes"
while choice == "yes":
    name = input("Enter your name: ").lower()
    bid_amount = int(input("How much would you like to bid? $"))
    bid[name] = bid_amount
    choice = input("Are there any more people in the room?\nEnter 'yes' or 'no' \n").lower()
    if choice != "yes":
        highest_bid(bid)
    elif choice == "yes":
        print("\n" * 50)

# python built-in max function
# max(bid, key = bid.get)