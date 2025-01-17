import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self, snake):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.75)
        self.color("yellow")
        self.penup()
        self.deploy_food(snake)

    def deploy_food(self, snake):
        while True:
            x1 = random.randint(-290, 290)
            y1 = random.randint(-290, 290)
            if not any(segment.distance(x1, y1) < 15 for segment in snake.segments):
                break
        self.goto(x1, y1)

    def did_you_eat(self, snake, score):
        if snake.segments[0].distance(self.xcor(), self.ycor()) < 15:
            snake.add_body()
            score.add_score()
            return True
        return False
