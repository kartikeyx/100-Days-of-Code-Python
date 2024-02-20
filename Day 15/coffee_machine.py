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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}
def is_resources_enough(ingredients):
  for item in ingredients:
    if ingredients[item] >= resources[item]:
      print(f"Sorry there is not enough {item}.")
      return False
  return True

def process_coins():
  print("Please insert coins.")
  total = int(input("How many quarters?: ")) * 0.25
  total += int(input("How many dimes?: ")) * 0.1
  total += int(input("How many nickles?: ")) * 0.5
  total += int(input("How many pennies?: ")) * 0.01
  return total


def is_transaction_success(money_recieved, drink_cost):
  if money_recieved >= drink_cost:
    change = round(money_recieved - drink_cost, 2)
    print(f"Here is ${change} in change.")
    global profit
    profit += drink_cost
    return True
  else:
    print(f"Sorry that's not enough money! Money refunded ${money_recieved}")
    return False


is_on = True

while is_on:
  choice = input("What would you like? (espresso/latte/cappuccino): ")
  if choice == "off":
    is_on = False
  elif choice == "report":
   print(f"Water: {resources["water"]}ml") 
   print(f"Milk: {resources["milk"]}ml" )   
   print(f"Coffee: {resources["coffee"]}g" )
   print(f"Money: ${profit}" )
  else:
    drink = MENU[choice]
    if is_resources_enough(drink["ingredients"]):
      payment = process_coins()
      is_transaction_success(payment, drink["cost"])