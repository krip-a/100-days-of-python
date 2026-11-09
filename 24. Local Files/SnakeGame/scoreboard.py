from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")
TEXT_COLOR = "white"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as data:
            self.high_score = int(data.read())
        self.penup()
        self.pencolor(TEXT_COLOR)
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """update score in scoreboard"""
        self.clear()
        self.write(arg= f"Score= {self.score} | High Score = {self.high_score}", align=ALIGNMENT,  font=FONT)


    def increase_score(self):
        """increase score by 1"""
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        """update the highscore"""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()


   
        