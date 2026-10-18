import turtle as t
import random

screen = t.Screen()                         # a new screen
screen.setup(width = 500, height = 400)     #set the screen size to 500x400
screen.title("TURTLE RACE!!!!")             #name the screen
screen.bgcolor("black")                     #set the screen color to black
user_bet = screen.textinput("Make your bet!", "Which turtle will win? Type a color.")

colors = ["red", "blue", "yellow", "green", "orange", "purple"]

turtles = []
for i in range(0, 6):
    new_turtle = t.Turtle("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-220, -100 + (i*40))
    turtles.append(new_turtle)

def banner(words, winner):
    banner = t.Turtle()
    banner.hideturtle()
    banner.penup()
    banner.color("red")
    banner.goto(0,0)
    banner.write("You " + words, align = "center", font = ("Arial", 30, "bold"))
    banner.goto(-50,-50)
    banner.write(f"The winner is {winner}", align = "center", font = ("Arial", 20, "bold"))

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:       
    for turtle in turtles:

        #each turtle is 40x40, X+ ends at 250. if first half reaches 250 then the coordinate is (230,y)
        # 250 - (40/2)
        if turtle.xcor() >= 230:                    
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                banner("won!", winning_color)
            else:
                banner("lost.", winning_color)
         
        turtle.forward(random.randint(0,10))
        

screen.exitonclick()

