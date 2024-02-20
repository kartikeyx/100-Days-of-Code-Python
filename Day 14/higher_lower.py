import random
import game_data
import art

def format_data(account):
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return f"{account["name"]}, a {account["description"]}, from {account["country"]}"

def check_answer(guess, a_followers, b_followers):
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


print(art.logo)
score = 0
game_continue = True
account_b = random.choice(game_data.data)

while game_continue:
  account_a = account_b
  account_b = random.choice(game_data.data)
  if account_a == account_b:
    account_b = random.choice(game_data.data)

  print(f"Compare A: {format_data(account_a)}")
  print(art.vs)
  print(f"Against B: {format_data(account_b)}")

  choice = input("Who has more followers? Type 'A' or 'B': ")

  a_followers= account_a["follower_count"]
  b_followers= account_b["follower_count"]

  is_correct = check_answer(choice, a_followers, b_followers)

  if is_correct:
    score += 1
    print(f"You're right! Current score: {score}.")
  else: 
    game_continue = False
    print(f"Sorry that's wrong. Final Score: {score}.")