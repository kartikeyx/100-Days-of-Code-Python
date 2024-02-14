import random
from art import logo

HARD_TURNS = 5
EASY_TURNS = 10
turns = 0
def check_answer(guess, answer, turns):
  
  if guess<answer:
    print("TOO LOW")
    return turns - 1
    
  
  elif guess>answer:
    print("TOO HIGH")
    return turns - 1
    
  
  else:
    print(f"YOU GOT IT. THE ANSWER WAS {answer}")

def difficulty_turns():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if difficulty == "hard":
    return HARD_TURNS
  else:
    return EASY_TURNS


def game():
  print(logo)
  print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
  
  turns=difficulty_turns()
  print(f"You have {turns} attempts remaining to guess the number.")
  num = random.randint(1, 100)
  guess = 0
  while guess!=num :
    print(f"You have {turns} attempts remaining to guess the number.")
    guess= int(input("Make a guess: "))
    turns = check_answer(guess, num, turns)
    if turns == 0:
      print("YOU RAN OUT OF TURNS")
      return 
    



game()