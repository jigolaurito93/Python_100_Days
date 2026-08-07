from turtle import Screen
import time
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=668, height=688)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

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


# def move_up():
#     new_segment.setheading(90)

# def move_down():
#     new_segment.setheading(270)
# def move_left():
#     new_segment.setheading(180)
# def move_right():
#     new_segment.setheading(0)

# screen.listen()
# screen.onkey(key="w", fun=move_up)
# screen.onkey(key="s", fun=move_down)
# screen.onkey(key="a", fun=move_left)
# screen.onkey(key="d", fun=move_right)

screen.exitonclick()