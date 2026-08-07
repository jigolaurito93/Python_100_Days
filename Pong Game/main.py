from turtle import Screen
from paddle import Paddle

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)


paddle1 = Paddle()

screen.listen()
screen.onkey(key="Up", fun=paddle1.go_up)
screen.onkey(key="Down", fun=paddle1.go_down)

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()