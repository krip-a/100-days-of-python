import turtle as t
import time

from snake import Snake

screen = t.Screen()
screen.setup(width=600, height=600)
screen.title("SNAKEEEEEE")
screen.bgcolor("black")
screen.tracer(n=0)                  #turning animation off until update is called
#screen.update()                     #screen will update only once this is called

snake = Snake()                     #creates the snake once triggered

#Automatically move the snake as 1 thing
game_is_on = True
while game_is_on:
    #delay the screen .1 seconds and see what happens
    screen.update()                 
    time.sleep(0.1)                   

    snake.move()                    #moves the snake 20 paces

    #move left or right
    screen.listen()
    screen.onkey(fun=snake.up, key="Up")
    screen.onkey(fun= snake.down, key="Down")
    screen.onkey(fun= snake.left, key="Left")
    screen.onkey(fun= snake.right, key="Right")










screen.exitonclick()