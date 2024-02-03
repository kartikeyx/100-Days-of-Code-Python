from art import logo
print(logo)

def add(numfirst, numsecond):
  return numfirst+numsecond
def sub(numfirst, numsecond):
  return numfirst-numsecond
def mult(numfirst, numsecond):
  return numfirst*numsecond
def divd(numfirst, numsecond):
  return numfirst/numsecond
  
operations = {"+": add,
              "-": sub, 
              "*": mult, 
              "/": divd
             }
def calculator1():
  num1 = float(input("What's the first number?: "))
  # char = input("+\n-\n*\n/\nPick an operation.")

  for symbol in operations:
    print(symbol)
  operation_symbol= input("Pick any operation from the line above: ")
  # function = operations[char]
  function = operations[operation_symbol]
  num2 = float(input("What's the second number?: "))
  answer = function(num1, num2)

  print(f"{num1} {operation_symbol} {num2} = {answer}")

  choice = False
  while not choice: 
    choose = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation, or 'q' to quit: ").lower()
    if choose == "y":
      operation_symbol = input("Pick another operation: ")
      num3 = float(input("What is the next number?: "))
      function = operations[operation_symbol]
      second_answer = function(answer, num3)
      print(f"{answer} {operation_symbol} {num3} = {second_answer}")

    elif choose == "n":
      choice = True
      calculator1()
    
    else:
      choice = True
      print("SHUT DOWN!")

calculator1()