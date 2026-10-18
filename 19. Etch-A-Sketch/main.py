import turtle as t

tim = t.Turtle()
screen = t.Screen()


def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_left():             #counterclockwise/left
    tim.left(10)

def turn_right():              #clockwise/right
    tim.right(10)

def clear_all():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    tim.setheading(0)

tim.pensize(5)
screen.listen()
screen.onkey(key = "w", fun = move_forward)     #don't use () w/ function, its passed as argument
screen.onkey(key = "s", fun = move_backward)
screen.onkey(key = "a", fun = turn_left)
screen.onkey(key = "d", fun = turn_right)
screen.onkey(key = "c", fun = clear_all)




screen.exitonclick()