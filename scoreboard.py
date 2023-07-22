from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-320, 320)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.color("white")
        self.write(f"Level : {self.level}", align="left", font=("Courier", 18, "normal"))
        
    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def gameover(self):
        self.goto(0, 0)
        self.color("white")
        self.write("GAME OVER.", align="center", font=("Courier", 18, "normal"))