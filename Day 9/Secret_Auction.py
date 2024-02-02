from art import logo
print(logo)
print("Welcome to the Secret Auction program.")
bids= {}

# def secret_bid(bid_name, bid_price):
#   empty_dic={}
#   empty_dic["name"] = bid_name
#   empty_dic["bid_price"]= bid_price
#   empty_lis.append(empty_dic)
def find_highest(bidding_record):
  high_price = 0
  for key in bidding_record:
    price = bidding_record[key]
    if high_price < price:
      high_price = price
      winner = key
  print(f"The winner is {winner} with the bid of ${high_price}")
bidding_end= False
while not bidding_end:
  name= input("What is your name? ")
  bid = int(input("What's your bid? $"))
  bids[name] = bid
  # secret_bid(bid_name=name, bid_price=bid)

  co= input("Are there any other bidders? Type'yes or 'no'.").lower()
  if co=="no":
    bidding_end= True
    find_highest(bids)
      