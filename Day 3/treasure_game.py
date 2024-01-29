#Project 3 Treasure game
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.\nYour mission is to find the Treasure.")

str1 = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\" \n").lower()
if str1== "left":
  str2 = input("You came to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across\n").lower()
  if str2 == "wait":
    str3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose.\n").lower()
    if str3=="red":
      print("IT'S A ROOM FULL OF FIRE. GAME OVER.")
    elif str3=="yellow":
      print("ROOM FULL OF TREASURE. YOU WON")
    elif str3=="blue":
      print("ROOM FULL OF BEASTS. GAME OVER.")
    else: 
      print("INVALID INPUT. GAME OVER.")
  else:
    print("YOU LOST THE GAME")  
else:
  print("YOU LOST THE GAME")

