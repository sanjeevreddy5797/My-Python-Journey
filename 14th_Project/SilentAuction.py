import artLogo
print(artLogo.logo)
print("----------Welcome to the Silent Auction----------")

bids={}
continue_bidding=True
while continue_bidding:
    name = input("What is your name? : ")
    price = int(input("What is your bid?: $"))
    bids[name] = price

    should_continue = input("Anyone are here to bid more? , Type 'yes' if you are intrested, Type 'no' if you are not : ").lower()

    if(should_continue == 'yes'):
        continue_bidding= True
    else:
        continue_bidding= False 

        highest_bid=max(bids.values())
        winner_name = max(bids,key = bids.get)      

        print(f"The winner is {winner_name} with a bid of ${highest_bid}.")