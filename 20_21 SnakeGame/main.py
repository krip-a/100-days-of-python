import turtle as t
import time

from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = t.Screen()
screen.setup(width=600, height=600)
screen.title("SNAKEEEEEE")
screen.bgcolor("black")
screen.tracer(n=0)                  #turning animation off until update is called
#screen.update()                     #screen will update only once this is called

snake = Snake()                     #creates the snake once triggered
food = Food()
scoreboard = Scoreboard()

#Automatically move the snake as 1 thing
game_is_on = True
while game_is_on:
    #delay the screen .1 seconds and see what happens
    screen.update()                 
    time.sleep(0.1)                   
    snake.move()                    #moves the snake 20 paces

    #detect collision w food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detect collision w wall
    if (snake.head.xcor() > 280 
        or snake.head.xcor() < -280 
        or snake.head.ycor() > 280 
        or snake.head.ycor() < -280):
        game_is_on = False                      #end game
        scoreboard.game_over()

    #detect collision w tail
       #if the head collides with any segment in the tail, trigger game over

    for segment in  snake.segments[1:]:    
        if snake.head.distance() < 10:
            #collision
            game_is_on = False
            scoreboard.game_over()

    #move left or right
    screen.listen()
    screen.onkey(fun=snake.up, key="Up")
    screen.onkey(fun= snake.down, key="Down")
    screen.onkey(fun= snake.left, key="Left")
    screen.onkey(fun= snake.right, key="Right")












screen.exitonclick()