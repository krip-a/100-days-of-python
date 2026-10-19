from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(n=0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# move paddle up and down
screen.listen()
screen.onkey(key= "Up", fun= r_paddle.paddle_up)
screen.onkey(key= "Down", fun= r_paddle.paddle_down)
screen.onkey(key= "w", fun= l_paddle.paddle_up)
screen.onkey(key= "s", fun= l_paddle.paddle_down)

def faster(time):
    new_time = time/10
    time.sleep(new_time)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)    
    screen.update()
    ball.move()

    #detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddles
    if (
        (ball.distance(r_paddle) < 50 and ball.xcor() > 320) 
        or
        (ball.distance(l_paddle) < 50 and ball.xcor() < -320)
        ):

        ball.bounce_x()
        

    #detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()










screen.exitonclick()