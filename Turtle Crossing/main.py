import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


player = Player()
screen.onkey(key="Up", fun=player.move)

cars = []
counter = 0


game_is_on = True
while game_is_on:
    counter += 1
    time.sleep(0.10)
    # time.sleep(0.05)
    screen.update()
    # if counter % 6 == 0:
    if counter % 20 == 0:
        cars.append(CarManager())
    for car in cars:
        car.drive()
        if player.distance(car) < 27:
            player.reset()
        if player.ycor() == 290:
            player.reset()
     