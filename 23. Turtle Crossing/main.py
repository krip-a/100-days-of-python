import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

timmy = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

#moving the turtle up
screen.listen()
screen.onkey(key="Up", fun= timmy.run)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #detect collision with car
    for car in car_manager.all_cars:
         if timmy.distance(car) < 20 or car.distance(timmy) < 20:
                scoreboard.end_game("GAME OVER")
                game_is_on = False

    #turtle hits the upper edge
    if timmy.is_at_finish_line():
          timmy.go_to_start()
          car_manager.level_up()                        #speed up
          scoreboard.update_level()
          #game_is_on = False


    


screen.exitonclick()