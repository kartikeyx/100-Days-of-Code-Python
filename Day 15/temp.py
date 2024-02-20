MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,False "milk": 200,
    "coffee": 100,
    "money": 0
}
def process(choice):
  if choice == "report":
    print(f"Water: {resources["water"]}ml") 
    print(f"Milk: {resources["milk"]}ml" )   
    print(f"Coffee: {resources["coffee"]}g" )
    print(f"Money: ${resources["money"]}" )
    return True
  elif choice == "end":
    print("COFFEE MACHINE CLOSE")
    return False
  elif choice == "espresso":
    if resources["water"] >50 and resources["milk"] > 0 and resources["coffee"] >18:
      resources["water"]-=50
      resources["coffee"]-=18
      money_input(choice)
      return True
    else:
      if resources["water"] < 50:
        print("Sorry there is not enough water.")
        return False
      else:
        print("Sorry there is not enough coffee.")
        return False
  elif choice == "latte":
    if resources["water"] >200 and resources["milk"] > 150 and resources["coffee"] > 24:
      resources["water"]-=200
      resources["milk"]-=150
      resources["coffee"]-=24
      money_input(choice)
      return True
    else:
      if resources["water"] < 200:
        print("Sorry there is not enough water.")
        return False
      elif resources["milk"] < 150:
        print("Sorry there is not enough water.")
        return False
      else:
        print("Sorry there is not enough coffee.")
        return False
  elif choice == "cappuccino":
    if resources["water"] >250 and resources["milk"] > 100 and resources["coffee"] >24:
      resources["water"]-=250
      resources["milk"]-=100
      resources["coffee"]-=24
      money_input(choice)
      return True
    else:
      if resources["water"] < 250:
        print("Sorry there is not enough water.")
        return False
      elif resources["milk"] < 100:
        print("Sorry there is not enough water.")
        return False
      else:
        print("Sorry there is not enough coffee.")
        return False
  
def money_input(choice):
  print("Please insert coins")
  quarters = float(input("How many quarters? "))
  dimes = float(input("How many dimes? "))
  nickles = float(input("How many nickles? "))
  pennies = float(input("How many pennies? "))
  cost = (0.25*quarters)+(0.10*dimes)+(0.05*nickles)+(0.01*pennies)
  if choice == "espresso":
    if cost < 1.5:
      print(f"Sorry that's not enough money. Money refunded {cost}")
    elif cost== 1.5:
      print(f"Here is your {choice} enjoy!")
    else:
      change=cost-1.5
      print(f"Here is your change {change:.2f}")
      print(f"Here is your {choice} enjoy!")
  elif choice == "latte":
    if cost < 2.5:
      print(f"Sorry that's not enough money. Money refunded {cost}")
    elif cost== 2.5:
      print(f"Here is your {choice} enjoy!")
    else:
      change=cost-2.5
      print(f"Here is your change {change:.2f}")
      print(f"Here is your {choice} enjoy!")

  else:
    if cost < 3.0:
      print(f"Sorry that's not enough money. Money refunded {cost}")
    elif cost == 3.0:
      print(f"Here is your {choice} enjoy!")
    else:
      change=cost-3.0
      print(f"Here is your change {change:.2f}")
      print(f"Here is your {choice} enjoy!")

  





def machine():
  while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    process(choice)
    return
  

machine()