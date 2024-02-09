

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from art import logo


def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  chosen_card= random.choice(cards)
  return chosen_card
def calculate_score(cards):
  if sum == 21 and len(cards==2):
    return 0
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)
def compare(u_score, c_score):
  if u_score == c_score:
    return "DRAW"

  elif u_score == 0:
    return "Win, you got blackjack"
  elif c_score == 0:
    return "Lose, opponent has Blackjack"
  elif u_score > 21:
    return "YOU LOSE SCORE OVER 21"
  elif c_score > 21:
    return "YOU WIN COMPUTER SCORE OVER 21"
  elif u_score > c_score:
    return "YOU WIN"
  else:
    return "YOU LOSE" 
      
def blackjack():
  print(logo)
  user_cards =[]
  computer_cards = [] 
  is_game_over = False
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  while not is_game_over: 
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
    print(f"Your cards:{user_cards} Your Score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]} ")
    if user_score == 0 or computer_score == 0 or user_score >21:
      is_game_over = True
    else:
      user_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
      if user_deal == "y":
        user_cards.append(deal_card())

      else:
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))


while input("Type 'y' to play new game or 'n' to quit: ").lower() == "y":
  blackjack()


