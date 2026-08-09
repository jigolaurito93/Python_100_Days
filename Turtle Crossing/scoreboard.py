from turtle import Turtle


FONT = ("Verdana", 24, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", font=FONT)
    
    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", font=FONT)
        self.goto(-280, 260)
    
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)