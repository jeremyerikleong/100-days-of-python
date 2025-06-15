import ascii_art


print("Welcome to the Secret Auction Program.")
print(ascii_art.logo)

def find_the_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of RM {highest_bid}")

bidders = {}
continue_bidding = True
while continue_bidding:
    bidder_name = input("What is your name?\n")
    amount = int(input("What is your bid?\n"))
    competitor = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    bidders[bidder_name] = amount

    if competitor == "no":
        continue_bidding = False
        find_the_highest_bidder(bidders)
    elif competitor == "yes":
        print("\n" * 20)



