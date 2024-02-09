import random
from art import logo
def guess():
  num = random.randint(1, 100)
  guess= int(input("Make a guess: "))
  if guess==num:
    print("YOU WIN")
  else:
    if guess>num:
      print("TOO HIGH")



def game():
  print(logo)
  print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  # turns = 0 
  # if difficulty == "easy":
  #   turns = 10
    
  # else:
  #   turns = 5

