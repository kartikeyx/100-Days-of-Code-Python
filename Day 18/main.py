# import colorgram
import turtle as t
import random
# rgb_colors =  []
# colors = colorgram.extract("Day 18\image.jpg", 30)
# for color in colors:
#   r = color.rgb.r
#   g = color.rgb.g
#   b = color.rgb.b
#   newcolor= (r,g,b)
#   rgb_colors.append(newcolor)
tim = t.Turtle()
tim.speed("fastest")
# print(rgb_colors)
t.colormode(255)
color_list = [(250, 246, 243), (248, 245, 246), (211, 154, 98), (53, 107, 131), (242, 249, 246), (235, 240, 244), (177, 78, 33), (198, 142, 35), (116, 155, 171), (124, 79, 98), (123, 175, 157), (226, 197, 130), (190, 88, 109), (12, 50, 64), (56, 39, 19), (41, 168, 128), (50, 126, 121), (199, 123, 143), (166, 21, 30), (224, 93, 79), (243, 163, 161), (38, 32, 34), (3, 25, 25), (80, 147, 169), (161, 26, 22), (21, 78, 90), (234, 167, 171), (171, 206, 190), (103, 127, 156), (165, 202, 210)]  
tim.penup()
tim.hideturtle()
screen = t.Screen()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_of_dots = 100

for dot_count in range (1, num_of_dots+1):
  
  tim.dot(20, random.choice(color_list))
  tim.forward(50)

  if dot_count%10 == 0:
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)


screen.exitonclick()