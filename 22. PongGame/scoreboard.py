from turtle import Turtle

SCOREBOARD_COLOR = "white"
ALIGNMENT = "center"
FONT = ("Courier", 40, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color(SCOREBOARD_COLOR)
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
            self.clear()
            #write left score
            self.goto(-100, 200)
            self.write(self.l_score, align= ALIGNMENT, font= FONT)
            #write right score
            self.goto(100, 200)
            self.write(self.r_score, align= ALIGNMENT, font= FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
    
