from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a colour: ")
colors=["indigo", "green", "red", "blue", "yellow", "orange"]
print(user_bet)
all_turtles = []
y=-100
for i in colors:
  new_turtle = Turtle("turtle")
  new_turtle.color(i)
  new_turtle.penup()
  y = y+30
  new_turtle.goto(x=-230, y=y)
  all_turtles.append(new_turtle)

if user_bet:
  is_race_on = True

while is_race_on:

  for turt in all_turtles:
    if turt.xcor() > 230:
      is_race_on = False
      winning_color = turt.pencolor()
      if winning_color == user_bet:
        print(f"You've Won! The {winning_color} is the winner.")
      else:
        print(f"You've Won! The {winning_color} is the winner.")
    rand_distance = random.randint(0,10)
    turt.forward(rand_distance)




screen.exitonclick()