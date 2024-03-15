from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    with open("Day 20/Snake-game/data.txt") as data:
      self.high_score = int(data.read())
    self.color("white")
    self.penup()
    self.goto(0,270)
    self.hideturtle()
    self.upd()
    
  def upd(self):
    self.clear()
    self.write(f"Score = {self.score} High Score = {self.high_score}", align = ALIGNMENT , font = FONT)

  def reset(self):
    if self.score > self.high_score:
      self.high_score = self.score
      with open("Day 20/Snake-game/data.txt", mode = "w") as data:
        data.write(f"{self.high_score}")
    self.score = 0
    self.upd()

  # def game_over(self):
  #   self.goto(0,0)
  #   self.write("GAME OVER", align = ALIGNMENT , font = FONT)

  def inc(self):
    self.score +=1
    
    self.upd()