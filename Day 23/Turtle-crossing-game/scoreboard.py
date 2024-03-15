from turtle import Turtle
FONT = ("Courier", 16, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.color("black")
    self.penup()
    self.goto(-230,240)
    self.score = 1
    self.hideturtle()
    self.upd()
    
  def upd(self):
    self.clear()
    self.write(f"Level = {self.score}", align = ALIGNMENT , font = FONT)

  def game_over(self):
    self.goto(0,0)
    self.write("GAME OVER", align = ALIGNMENT , font = FONT)

  def inc(self):
    self.score +=1
    self.upd()