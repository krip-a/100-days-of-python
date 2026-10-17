#from turtle import Turtle, Screen
#from turtle import *
import turtle as t
import random

t.colormode(255)

tim = t.Turtle()
tim.shape("turtle")
tim.color("CadetBlue2")


color_list = ["DarkCyan", "cyan", "blue", "red", 
              "yellow", "DarkOrange", "DeepPink", 
              "DarkOliveGreen", "orchid", "purple"
              ]

#direction_list = ["left", "right", "forward", "backward"]
direction_list = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_col = (r, g, b)
    return random_col

def square():
    for _ in range (0, 4):
        tim.forward(100)
        tim.left(90)



def dash_line():
    for _ in range(20):
        tim.forward(5)
        tim.penup()
        tim.forward(5)
        tim.pendown()


def shapes():
    for i in range(3, 11):
        j = int(360 / i)
        color = random.choice(color_list)
        tim.pencolor(color)
        for _ in range(0, i):
            tim.forward(100)
            tim.right(j)


def random_walk():
    tim.pensize(20)
    tim.speed("fastest")
    for _ in range(200):
        #tim.pencolor(random.choice(color_list))
        tim.pencolor(random_color())
        tim.forward(50)
        tim.setheading(random.choice(direction_list))
   
def draw_spirograph(size_of_gap):
    tim.speed("fastest")
    for _ in range((int(360/size_of_gap))):
        tim.pencolor(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)
        

#square()
#dash_line()
#shapes()
#random_walk()
draw_spirograph(10)
screen = t.Screen()
screen.exitonclick()