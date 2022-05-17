import colorgram
from turtle import Screen
from turtle import Turtle
import random

# colors = colorgram.extract('BjKAyjP0hlnK_2400x2400.jpg', 30)

# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colors = (r, g, b)
#     rgb_colors.append(new_colors)
#
# print(rgb_colors)

n_rgb_colors = [(243, 243, 245), (244, 240, 232), (244, 237, 242), (236, 243, 240), (214, 154, 105), (49, 96, 139),
                (163, 80, 45), (223, 209, 107), (17, 36, 59), (185, 163, 25), (120, 163, 202), (56, 30, 18),
                (126, 68, 94), (210, 91, 69), (43, 128, 70), (193, 140, 160), (162, 20, 10), (125, 181, 156),
                (58, 28, 40), (129, 26, 42), (19, 52, 43), (194, 91, 113), (48, 170, 98), (39, 62, 97), (27, 91, 52),
                (235, 162, 187), (108, 118, 172), (225, 206, 2), (6, 88, 108), (227, 179, 170)]

screen = Screen()

screen.colormode(255)
tim = Turtle("arrow")
tim.penup()
tim.setx(-200)
tim.sety(-200)

def line():
    for i in range(10):
        tim.pencolor(random.choice(n_rgb_colors))
        tim.dot(15)
        tim.forward(40)

def turn():
    tim.setheading(90)
    tim.penup()
    tim.forward(40)

coordinate = -200

for i in range(10):
    line()
    coordinate += 40
    tim.sety(coordinate)
    tim.setx(-200)
    


screen.exitonclick()
