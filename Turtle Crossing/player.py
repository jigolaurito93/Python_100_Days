from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.setheading(90)
        self.shape('turtle')
        self.goto(0, -270)
    
    def move(self):
        self.forward(10)