from turtle import Turtle, Screen
import random


tim = Turtle()
tim.shape("turtle")
tim.color("red")
tim.pencolor("black")
# for _ in range(4):  # Loop four times
#     tim.forward(100)
#     tim.left(90)
# for _ in range(5):  # Repeat twice for a dash
#     tim.forward(10)
#     tim.penup()
#     tim.forward(5)
#     tim.pendown()
# for _ in range(3):
#     tim.forward(100)
#     tim.left(120)
# for _ in range(4):  # Loop four times
#     tim.forward(100)
#     tim.left(90)
# for _ in range(5):  # Loop four times
#     tim.forward(100)
#     tim.left(72)
# for _ in range(6):  # Loop four times
#     tim.forward(100)
#     tim.left(60)
# for _ in range(7):  # Loop four times
#     tim.forward(100)
#     tim.left(51)
# for _ in range(8):  # Loop four times
#     tim.forward(100)
#     tim.left(45)
# for _ in range(9):  # Loop four times
#     tim.forward(100)
#     tim.left(40)
#     for _ in range(4):  # Loop four times
#         tim.forward(100)
#         tim.left(90)

def shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.left(angle)

def get_random_color():
  # Generate random values between 0 and 255 for red, green, and blue
  r = random.randint(0, 255)/255
  g = random.randint(0, 255)/255
  b = random.randint(0, 255)/255
  # Return a tuple representing the RGB color
  return (r, g, b)


        
# for shape_side in range(3, 11):
#     tim.pencolor(get_random_color())
#     shape(shape_side)

direction = [0, 90, 180, 270]

tim.pensize(6)
for i in range(50):
    tim.pencolor(get_random_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))









screen = Screen()
screen.exitonclick()
Turtle.hideturtle()
Turtle.done()