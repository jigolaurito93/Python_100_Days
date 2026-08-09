from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scorebored(Turtle):
    def __init__(self):
        super().__init__()
        with open("Snake Game/high_score.txt", mode="r") as high_score_file:
            self.high_score =  int(high_score_file.read())
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(-110, 300)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=(FONT))
        self.goto(90, 300)
        self.write(f"High Score: {self.high_score}", align=ALIGNMENT, font=(FONT))
        self.hideturtle()
    
    def update_score(self):
        self.goto(-110, 300)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=(FONT))
        self.goto(90, 300)
        self.write(f"High Score: {self.high_score}", align=ALIGNMENT, font=(FONT))
    
    def add_point(self):
        self.score += 1
        self.clear()
        self.update_score()
    
    def update_high_score(self):
        if self.score > self.high_score:
            # Open file, overwrite the score
            with open("Snake Game/high_score.txt", mode="w") as high_score_file:
                high_score_file.write(f"{self.score}")
            # Open file, grab the file and convert to integer, store in variable
            with open("Snake Game/high_score.txt") as high_score_file:
                self.high_score = int(high_score_file.read())

    def reset(self):
        self.update_high_score()
        self.clear()
        self.score = 0
        self.update_score()
