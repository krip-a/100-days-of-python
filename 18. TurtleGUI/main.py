import turtle as t
import random

color_list = [
    (202, 164, 110), (240, 245, 241), (236, 239, 243), 
    (149, 75, 50), (222, 201, 136), (53, 93, 123), 
    (170, 154, 41), (138, 31, 20), (134, 163, 184), 
    (197, 92, 73), (47, 121, 86), (73, 43, 35), 
    (145, 178, 149), (14, 98, 70), (232, 176, 165), 
    (160, 142, 158), (54, 45, 50), (101, 75, 77),
    (183, 205, 171), (36, 60, 74), (19, 86, 89), 
    (82, 148, 129), (147, 17, 19), (27, 68, 102), 
    (12, 70, 64), (107, 127, 153), (176, 192, 208), 
    (168, 99, 102)
    ]
#change the color mode to use rgb
t.colormode(255)

tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)         #halfway between 180 and 270 so it starts in a corner
tim.forward(300)
tim.setheading(0)

def random_color():
    return random.choice(color_list)

number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random_color())
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()