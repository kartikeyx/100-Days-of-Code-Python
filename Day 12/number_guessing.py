import random
from art import logo

HARD_TURNS = 5
EASY_TURNS = 10

def gu():
  num = random.randint(1, 100)
  guess= int(input("Make a guess: "))
  if guess==num:
    print("YOU WIN")
  else:
    if guess>num:
      print("TOO HIGH")

def difficulty_turns(difficulty):
  if difficulty == "hard":
    return HARD_TURNS
  else:
    return EASY_TURNS


def game():
  print(logo)
  print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  difficulty_turns(difficulty)
  



