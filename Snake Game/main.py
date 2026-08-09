from turtle import Screen, update
import time
from snake import Snake
from food import Food
from scoreboard import Scorebored

screen = Screen()
screen.setup(width=668, height=688)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scorebored()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
# screen.update()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    # Detect the collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_point()
    
    # Detect wall collision
    if snake.head.xcor() > 320 or snake.head.xcor() < -320 or snake.head.ycor() > 320 or snake.head.ycor() < -320:
        snake.reset()
        scoreboard.reset()
        screen.update()

    
    # Detect collision with tail
    for segment in snake.segments[1:len(snake.segments) + 1]:
        if snake.head.distance(segment) < 10:
            snake.reset()
            scoreboard.reset()
            screen.update()




screen.exitonclick()