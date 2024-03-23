#in vs code I need to do :
#py -m pip install replit
from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
bids = {}
more_bidders = True
print(logo)

def bidding():
    while more_bidders is True:
        bidder_name = input("What is your name?:")
        bidder_bid = int(input("What's your bid?: "))
        bids.update({bidder_name:bidder_bid})
        more_bid = input("Is there another bidder? 'yes' or 'no'?")
        if more_bid == 'yes':
            clear()
        elif more_bid == 'no':
            more_bidders == False
            return bids

bidding()

highest_bid = 0
highest_bidder = ''

for bidder in bids:
    bid_amount= bids[bidder]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        highest_bidder = bidder 

print(f"The highest bidder is {highest_bidder} winning with a bid of ${highest_bid}.")
