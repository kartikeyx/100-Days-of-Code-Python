import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")
screen = t.Screen()
t.colormode(255)
# colour = [ "red", "blue", "green", "yellow", "purple", "orange", "black","pink" ]
tim.pensize(1)
tim.speed("fastest")
def random_color():
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  c = (r,g,b)
  return c
# for i in range(3):
#   tim.color("red")
#   tim.forward(100)
#   tim.right(60)

# for i in range(4):
#   tim.color("blue")
#   tim.forward(100)
#   tim.right(90)

# for i in range(5):
#   tim.color("darkorange")
#   tim.forward(100)
#   tim.right(72)
# for i in range(6):
#   tim.color("gold")
#   tim.forward(100)
#   tim.right(60)
# for i in range(7):
#   tim.color("limegreen")
#   tim.forward(100)
#   tim.right(51.42)
# for i in range(8):
#   tim.color("peru")
#   tim.forward(100)
#   tim.right(45)
# for i in range(9):
#   tim.color("wheat")
#   tim.forward(100)
#   tim.right(40)
# for i in range(10):
#   tim.color("black")
#   tim.forward(100)
#   tim.right(36)
# for i in range(5):
#   tim.forward(10)
#   tim.penup()
#   # tim.color("white")
#   tim.forward(10)
#   tim.pendown()
#   # tim.color("black")

# def draw_shape(num_sides):
#   angle = 360/num_sides
#   for _ in range(num_sides):
#     tim.forward(100)
#     tim.right(angle)

# for shape_side_n in range(3,11):
#   tim.color(random.choice(colour))
#   draw_shape(shape_side_n)
# def is_in_screen(screen, tim):
#   if random.random()>0.1:
#     return True
#   else:
#     return False

# while is_in_screen(screen, tim):
#   tim.color(random.choice(colour))
#   coin = random.randrange(0,2)
#   if coin ==0:
#     tim.left(90)
#   else:
#     tim.right(90)

#   tim.forward(50)
# directions=[0,90,180,270]

# for _ in range(200):
#   tim.color(random_color())
#   tim.forward(20)
#   tim.setheading(random.choice(directions))

for i in range(450):
  tim.color(random_color())
  tim.circle(100)
  tim.left(1)


screen.exitonclick()