from turtle import Screen
import time
from crossingturtle import CrossingTurtle
from carManager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(700, 700)
screen.title("Turtle Crossing Game")
screen.tracer(0)

playerTurtle = CrossingTurtle()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(playerTurtle.moveup, "Up")


sleeptime = 0.1
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(sleeptime)

    cars.create_car()
    cars.move()

    #Detect collision with car
    for car in cars.allcars:
        if car.distance(playerTurtle) < 20:
            score.gameover()
            game_is_on = False

    #Detect collision with wall
    for car in cars.allcars:
        if playerTurtle.ycor() > 330:
            score.increase_level()
            sleeptime -= 0.01
            playerTurtle.goto(0, -320)





screen.exitonclick()