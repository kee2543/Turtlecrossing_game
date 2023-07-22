from turtle import Turtle

class CrossingTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.goto(0, -295)
        self.shape("turtle")
        self.color("#D9D7F1")
        self.penup()
        self.setheading(90)
        self.shapesize(1.3, 1.3)

    def moveup(self):
        self.forward(20)
        