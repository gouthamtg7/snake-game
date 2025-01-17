import turtle
from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.displayscore = 0
        self.score_display = Turtle()
        self.score_display.color("orange")
        self.score_display.penup()
        self.score_display.hideturtle()
        self.score_display.goto(-150, 220)

        with open("highscore.txt") as data:
            self.highscore = int(data.read())

        self.high = Turtle()
        self.high.color("green")
        self.high.penup()
        self.high.hideturtle()
        self.high.goto(100, 220)

    def add_score(self):
        self.displayscore += 1
        self.high_score()

    def display(self):
        self.score_display.clear()  # Clear previous score display
        self.score_display.write(f"Score: {self.displayscore}", align="center", font=("Arial", 16, "normal"))
        self.display_highscore()

    def high_score(self):
        if self.displayscore > self.highscore:
            self.highscore = self.displayscore
            with open("highscore.txt", mode="w") as data:
                data.write(f"{self.highscore}")

    def display_highscore(self):
        self.high.clear()  # Clear previous high score display
        self.high.write(f"High Score: {self.highscore}", align="center", font=("Arial", 16, "normal"))
