from turtle import Turtle
import random

COLOURS = ["#6E5773", "#D45079", "#EA9085", "#E9E1CC", "#F9CC7B", "#6DB3B5", "#7AA5D2", "#9EDE73"]

class CarManager:
    def __init__(self):
        self.allcars = []

    def create_car(self):
        chance = random.randint(1, 5)
        if chance == 1 or chance == 5:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLOURS))
            random_y = random.randint(-250, 250)
            new_car.goto(320, random_y)
            self.allcars.append(new_car)

    def move(self):
        for car in self.allcars:
            car.backward(20)
        

