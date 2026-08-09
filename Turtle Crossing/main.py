import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()


player = Player()
screen.onkey(key="Up", fun=player.move)
# screen.onscreenclick(lambda x, y: player.move(), btn=1)

cars = []
counter = 0
speed = .10

game_is_on = True
while game_is_on:
    counter += 1
    time.sleep(speed)
    screen.update()
    # if counter % 20 == 0:
    if counter % 6 == 0:
        cars.append(CarManager())
    for car in cars:
        car.drive()
        # Player goes to start when collides with car

        if player.distance(car) < 27:
            player.reset()
            game_is_on = False

        # Player goes to start when crosses finish line
        # Player levels up
        if player.ycor() == 290:
            player.reset()
            scoreboard.level_up()
            speed -= .01
            print(speed)

scoreboard.game_over()

screen.exitonclick()