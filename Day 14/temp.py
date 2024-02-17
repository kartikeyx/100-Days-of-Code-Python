import random
import game_data
import art
print(art.logo)
score = 0
def compare(choice, a, b):
  if a["follower_count"] > b["follower_count"]:
    if choice == "A":
      return True
    else:
      return False
  else:
    if choice == "A":
      return False
    else:
      return True

def choices():
  global a 
  global b 
  a = random.choice(game_data.data)
  b = random.choice(game_data.data)

def game(a,b):

  print(f"Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}")
  print(art.vs)
  print(f"Against B: {b["name"]}, a {b["description"]}, from {b["country"]}")
  choice = input("Who has more followers? Type 'A' or 'B': ")

  game_cont = compare(choice, a, b)
  while game_cont:
    score+=1
    print(f"You're right! Current score: {score}.")
    a=b
    b = random.choice(game_data.data)
    game(a,b)

  print(f"Sorry that's wrong. Final score: {score}")
  return



game(a,b)