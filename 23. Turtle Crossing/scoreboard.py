from turtle import Turtle

FONT = ("Courier", 24, "normal")
LEVEL_POSITION = (-200, 250)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.penup()
        self.level = 0
        self.update_level()

    def end_game(self, text):
        self.goto(0,0)
        self.color("red")
        self.write(arg = f"{text}", align= "center", font= FONT)

    def update_level(self):
        self.clear()
        self.color("yellow")
        self.level += 1
        self.goto(LEVEL_POSITION)
        self.write_level()

    def write_level(self):
        self.write(f"Level: {self.level}", align= "center", font= FONT)
        
