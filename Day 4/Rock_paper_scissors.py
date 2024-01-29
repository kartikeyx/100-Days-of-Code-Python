#Day 4 Rock Paper And Scissors
import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
gg=[rock, paper, scissor]

choice1 = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors."))
if choice1 > 2 or choice1 < 0:
  print("YOU TYPED AN INVALID NUMBER. YOU LOSE")
else: 
  print(f"You chose {gg[choice1]}")
  choice2 = random.randint(0,2)
  print(f"Computer chose {gg[choice2]}")

  if choice1==choice2:
    print("DRAW")
  elif choice1 == 0 and choice2 == 1:
    print("YOU LOSE")
  elif choice1 == 0 and choice2 == 2:
    print("YOU WIN")
  elif choice1 > choice2:
    print("YOU WIN")
  elif choice1 < choice2:
    print("YOU LOSE")
  elif choice1 > 2 or choice1 < 0:
    print("YOU TYPED AN INVALID NUMBER. YOU LOSE")
