#Project 2 Tip Generator

print("Welcome to the Tip Genrator")
bill= float(input("What was your total bill?\n"))
tip_per= float(input("What percentage tip would you like to give?\n"))
num_peo= int(input("How many people will split the bill?\n"))


sp= str((bill*tip_per/100)/num_peo)
print("Each person should pay: " +sp)